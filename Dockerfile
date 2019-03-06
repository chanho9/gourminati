FROM python:3.6-alpine
MAINTAINER phdpark <pch881125@gmail.com>

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt
ENV FLASK_APP=gourminati.py
RUN flask init-db
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]

EXPOSE 80