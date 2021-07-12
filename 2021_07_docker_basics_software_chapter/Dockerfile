FROM python:3.9.6-slim

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY main.py ./tmp

CMD ["python3", "./tmp/main.py"]
