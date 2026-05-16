# Use lightweight Python image
FROM python:3.10-slim

# Prevent Python buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Set dummy env vars for build time only
ENV SECRET_KEY=dummy-build-secret-key-not-used-in-production
ENV DEBUG=True
ENV DB_ENGINE=django.db.backends.sqlite3

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Run migrations then start Gunicorn
CMD ["sh", "-c", "python manage.py migrate && gunicorn --bind 0.0.0.0:8000 leave_project.wsgi:application"]
