# Use Python base image
FROM python:3.10

# Set working directory
RUN mkdir /code
WORKDIR /code

# Copy application code
ADD . /code
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5000

# Run the application
CMD ["python3", "/code/run.py"]