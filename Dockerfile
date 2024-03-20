# Select base Python environment
FROM python:3.8-slim AS base

# Set the working directory in the container
WORKDIR /app

# Copy all content from the repository into the created directory
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py

# Command to run when the container starts
CMD ["flask", "run", "--host=0.0.0.0"]
