FROM python:3.11

RUN apt-get update -y

RUN mkdir /app

WORKDIR /app

COPY app/requirements.txt ./

RUN pip install -U pip

RUN pip install -r requirements.txt

COPY app/ ./

EXPOSE 8080

ENTRYPOINT ["python","main.py"]