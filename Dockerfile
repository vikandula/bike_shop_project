FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Flask
RUN pip install flask

# Expose Flask port
EXPOSE 5050

# Run application
CMD ["python", "app.py"]
