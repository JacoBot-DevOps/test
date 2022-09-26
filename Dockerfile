# dockerfile for webserver3(flask framework)


FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

# EXPOSE 6000

CMD ["python", "app.py"]