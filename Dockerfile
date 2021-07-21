FROM python:3.8.3-slim-buster

COPY . /build

WORKDIR /build

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
