FROM python:latest

COPY requirements.txt .

RUN ["pip", "install", "-r", "requirements.txt"]

COPY db.py .

RUN ["python3", "db.py"]

COPY . .

CMD ["python3", "main.py"]