FROM python:3.9-slim

WORKDIR /app

# Copy requirements with vulnerable packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application with secrets (bad practice - will be detected)
COPY app.py .
COPY config.py .
COPY secrets.env .

EXPOSE 5000
CMD ["python", "app.py"]
