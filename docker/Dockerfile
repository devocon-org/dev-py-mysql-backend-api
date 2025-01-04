# docker/Dockerfile
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY app/ /app/

CMD ["python", "app.py"]

