# сборка и запуск контейнера описан в README!!!

FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /var/app

COPY requirements.txt ./
RUN python -m pip install -r requirements.txt

COPY my_app ./
 
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
