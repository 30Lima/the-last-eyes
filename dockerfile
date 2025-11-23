# Base Image
FROM python:3.10-slim

# Directory
WORKDIR /app

# Installing system dependencies
RUN apt-get update && apt-get install -y build-essential

# Copying the requirements and installing
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copying the project
COPY . .

# Exposing the default render port
EXPOSE 10000

# Starting FastAPI
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT}"]
