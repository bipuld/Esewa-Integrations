# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (if needed)
# RUN apt-get update && apt-get install -y some-package

# Copy the Django project files into the container
COPY . /app/

# Install Django and other Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the application will run on
EXPOSE 8000

# Run migrations and start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
