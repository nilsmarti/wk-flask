FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

# Ensure the database directory exists
RUN mkdir -p /app/data
RUN touch /app/data/wanikani.db
RUN chmod 666 /app/data/wanikani.db

# Initialize database
RUN python3 -c 'from app import init_db; init_db()'

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]

