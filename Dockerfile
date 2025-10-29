FROM python:3.10-slim

WORKDIR /app

# install required packages for system
RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev pkg-config curl && \
    rm -rf /var/lib/apt/lists/*


COPY requirements.txt /app

RUN pip install mysqlclient
RUN pip install --no-cache-dir -r requirements.txt

COPY /src /app

CMD ["python","app.py"] 
