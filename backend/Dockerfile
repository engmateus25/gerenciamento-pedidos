FROM python:3.10

RUN apt-get update && apt-get install -y default-mysql-client

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /app/wait-for-db.sh

EXPOSE 8000

CMD ["/bin/sh", "-c", "./wait-for-db.sh"]
