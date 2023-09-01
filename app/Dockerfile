FROM python:3

WORKDIR /FLASK_APP/

COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN chnod -R 777 /app

ENTRYPOINT FLASK_APP= /app/app.py flask run --host=0.0.0.0
EXPOSE 8008