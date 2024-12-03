"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from typing import List, Dict
import aiohttp
from models import Base, engine, Session, User, Post
from jsonplaceholder_requests import fetch_users, fetch_posts


async def add_users_to_db(session_db: Session, users: List[Dict]):
    user_objects = []
    for user in users:
        user_obj = User(
            id=user['id'],
            name=user['name'],
            username=user['username'],
            email=user['email']
        )
        user_objects.append(user_obj)
    session_db.add_all(user_objects)
    await session_db.commit()

async def add_posts_to_db(session_db: Session, posts: List[Dict]):
    post_objects = []
    for post in posts:
        post_obj = Post(
            id=post['id'],
            user_id=post['userId'],
            title=post['title'],
            body=post['body']
        )
        post_objects.append(post_obj)
    session_db.add_all(post_objects)
    await session_db.commit()


async def async_main():
    """
    Основная функция
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with aiohttp.ClientSession() as http_session:
        try:
            users_task = fetch_users(http_session)
            posts_task = fetch_posts(http_session)
            users_data, posts_data = await asyncio.gather(users_task, posts_task)
        except Exception as e:
            return

    async with Session() as db_session:
        try:
            await add_users_to_db(db_session, users_data)
            await add_posts_to_db(db_session, posts_data)
        except Exception as e:
            print(f"Ошибка при добавлении данных в базу: {e}")
            return

    await engine.dispose()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    asyncio.run(main())