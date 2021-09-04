FROM python:3-alpine
ENV PYTHONUNBUFFERED=1
RUN apk add gcc jpeg-dev zlib-dev musl-dev 
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
