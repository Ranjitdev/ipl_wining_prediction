FROM python:3.9-slim
COPY . /app
WORKDIR /app
EXPOSE $PORT
RUN pip install -r requirements.txt
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
CMD streamlit run app.py