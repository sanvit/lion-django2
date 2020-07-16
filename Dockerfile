FROM python:3.8.3

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY . /app
RUN pip install -r /app/requirements.txt
RUN chmod 755 /app/app.sh
WORKDIR /app
EXPOSE 8000

ENTRYPOINT ["/app/app.sh"]