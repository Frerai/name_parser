# Use an official Python image as the base image.
FROM python:3.10

# Set the working directory.
WORKDIR /app

# Copy the required files into the container.
COPY . .

# Install required packages.
RUN pip install --no-cache-dir -r requirements.txt


# Set the environment variable for the service.
ENV PYTHONUNBUFFERED 1

# Expose the port used by the service.
EXPOSE 8200

# Define the command to run when the container starts.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8200"]
