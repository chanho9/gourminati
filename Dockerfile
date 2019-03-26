FROM python:3.6-alpine
MAINTAINER phdpark <pch881125@gmail.com>

COPY . /app
WORKDIR /app

RUN mkdir -p /mnt/data
ENV GOURMINATI_DATA_PATH=/mnt/data/gourminati.xlsx
ENV GOURMINATI_KAKAO_API_KEY="Enter API key"

RUN pip3 install -r requirements.txt
ENV FLASK_APP=gourminati.py
CMD flask init-db && flask run --host=0.0.0.0 --port 80

EXPOSE 80