# Use an official Python runtime as a parent image
FROM huggingface/transformers-pytorch-gpu

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Expose port 8000 for the FastAPI app
EXPOSE 8000

# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "deploy-nlp-summarize:app", "--host", "0.0.0.0", "--port", "8000"]
