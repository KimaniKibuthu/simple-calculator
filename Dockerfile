# Set python image
FROM python:3.11-slim-bullseye

# Set work directory
WORKDIR /app

# Copy source code to the container
COPY . /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port where the Streamlit app will run
EXPOSE 8501

# Command to run the Streamlit application
CMD ["streamlit", "run", "app.py", "--server.port", "8501"]