FROM python:3.11-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y build-essential libpq-dev poppler-utils --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY src/ /app/src
WORKDIR /app
ENV PYTHONPATH="/app/src:${PYTHONPATH:-}"
CMD ["python", "-m", "src.cli"]
