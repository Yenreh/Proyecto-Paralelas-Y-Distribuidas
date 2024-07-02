FROM python:3.12-slim

WORKDIR /frontend_app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application
COPY . .

# Set permissions for all files under /frontend_app
RUN chmod -R 777 /frontend_app


