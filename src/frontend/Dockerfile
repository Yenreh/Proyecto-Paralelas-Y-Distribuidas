FROM python:3.12-slim

WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application
COPY . .
RUN chmod -R 777 /app
RUN chmod -R 777 /app/src/config
EXPOSE 5000
CMD ["python3.12", "/app/src/run.py"]


