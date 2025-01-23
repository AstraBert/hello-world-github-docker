# Define your python version
ARG PY_VERSION="3.11.9-slim-bookworm"

# Base image
FROM python:${PY_VERSION}

# Define your working directory
WORKDIR /app/
# Copy your local file system into the working directory
COPY ./ /app/

# Install the necessary dependencies
RUN pip cache purge
RUN pip install --no-cache-dir -r requirements.txt

# Run the application as an entrypoint
ENTRYPOINT python3 app.py
