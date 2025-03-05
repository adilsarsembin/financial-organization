FROM python:3.12

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libc-dev \
    libpq-dev \
    libgdal-dev \
    gdal-bin \
    && pip install --no-cache-dir --upgrade pip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy and install Python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PATH="/usr/local/bin:$PATH"

# Expose port
EXPOSE 8000

# Run Gunicorn
CMD ["gunicorn", "financial_organization.wsgi:application", "--workers", "2", "--threads", "4", "--bind", "0.0.0.0:8000"]
