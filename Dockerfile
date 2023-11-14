# Use an official Python runtime as a parent image
FROM python:3-alpine3.16

# Set the working directory to /app
WORKDIR /FLASK-PROJECT


# Copy the current directory contents into the container at /app
COPY . /FLASK-PROJECT

RUN apt-get update && apt-get install -y \ 
    python-opencv

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5001

# Define the command to run your application
CMD ["python", "main.py"]