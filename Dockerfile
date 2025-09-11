# Use an official lightweight Python image as the base
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker's build cache
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Tell Cloud Run what command to run, using the $PORT variable it provides
CMD ["sh", "-c", "adk api_server . --host=0.0.0.0 --port $PORT --session_service_uri='sqlite:///adk_sessions.db'"]

# Use adk web instead of adk api_server!
# CMD ["sh", "-c", "adk web --port $PORT"]