# Use Python image
FROM python:3.10

# Set working directory in container
WORKDIR /app

# Copy code into container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start your app
CMD ["tail", "-f", "/dev/null"]
