# Use Python 3.11 slim image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies directly
RUN pip install --upgrade pip
RUN pip install Django==5.2.3 \
    djangorestframework \
    djangorestframework-simplejwt \
    python-decouple \
    gunicorn

# Copy project
COPY . /app/

#Create and copy the startup script
COPY startup.sh /app/startup.sh
RUN chmod +x /app/startup.sh

# Expose port
EXPOSE 8000

# Run the application
CMD ["/app/startup.sh"]