FROM python:3.9-slim
COPY . /app
WORKDIR /app
EXPOSE $PORT
RUN pip install -r requirements.txt
