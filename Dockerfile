FROM python:3.11

ENV PYTHONUNBUFFERED=1

#assign a working directory
WORKDIR /app

RUN apt-get update -y && apt-get install netcat -y
RUN apt-get upgrade -y && apt-get install postgresql gcc python3-dev musl-dev -y

#install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

#copy the project to the working directory
COPY .  /app

#ENTRYPOINT sh -c /app/entrypoint.sh
