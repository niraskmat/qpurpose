FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x /app/wait_for_db.sh

CMD ["./wait_for_db.sh", "db", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
