FROM python:3.12-slim

WORKDIR /backend

EXPOSE 50051

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

COPY . /backend

CMD ["python", "server.py"]
