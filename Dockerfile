FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD flask --app app --debug run --port 8000 --host 0.0.0.0