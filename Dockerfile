FROM python:3.6
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD ./ app

RUN pip install -r requirements.txt

