FROM python:3.9

# Install netcat (specifically netcat-openbsd)
RUN apt-get update && apt-get install -y netcat-openbsd

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["sh", "wait_for_db.sh"]
