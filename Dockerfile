# Use a lightweight Python base image
FROM python:3.12-alpine3.21

# Set the maintainer (optional)
LABEL maintainer="kattchiie"

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Create a non-root user early to improve security
RUN addgroup -S django && adduser -S django-user -G django

# Set the working directory
WORKDIR /app

# Copy dependencies file first to leverage Docker cache
COPY requirements.txt /tmp/requirements.txt
COPY requirements.dev.txt /tmp/requirements.dev.txt

# Define the DEV argument (use again before RUN to optimize caching)
ARG DEV=false

# Install dependencies efficiently
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt && \
    if [ "$DEV" = "true" ];\
        then pip install --no-cache-dir -r /tmp/requirements.dev.txt; \
    fi &&\
    rm -rf /tmp

# Copy the application code
COPY . .

# Expose port for the application
EXPOSE 8000

# Set the user to avoid running as root
USER django-user

# Default command (optional, adjust as needed)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
