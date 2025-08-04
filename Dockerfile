# Use Python 3.11
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy everything into container
COPY . .

# Upgrade pip
RUN pip install --upgrade pip

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port used by the Flask app
EXPOSE 10000

# Start the Flask app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]
