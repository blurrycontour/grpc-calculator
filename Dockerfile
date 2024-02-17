FROM python:3.12

WORKDIR /backend

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

COPY . /backend
RUN make clean && make

CMD ["python", "server.py"]
