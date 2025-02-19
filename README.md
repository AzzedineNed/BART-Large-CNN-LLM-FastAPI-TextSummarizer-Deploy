# **BART-Large-CNN-LLM-FastAPI-TextSummarizer-Deploy**

This project provides a **Text Summarization API** using the **BART model** (from Hugging Face's Transformers library), deployed using **FastAPI** and **Docker**. It allows users to input text and receive a summarized version of that text. The application also provides a simple frontend built with HTML and JavaScript to interact with the backend API.

<p align="center">
  <img src="https://github.com/AzzedineNed/BART-Large-CNN-LLM-FastAPI-TextSummarizer-Deploy/blob/master/screenshots/UI1.PNG" alt="Screenshot 1" width="500">
</p>
<p align="center"><em>Screenshot of the Text Summarizer Interface (before the backend service is fully started)</em></p>

<p align="center">
  <img src="https://github.com/AzzedineNed/BART-Large-CNN-LLM-FastAPI-TextSummarizer-Deploy/blob/master/screenshots/UI2.PNG" alt="Screenshot 2" width="500">
</p>
<p align="center"><em>Screenshot of the Text Summarizer Interface with the summarized text</em></p>


## **Project Structure**

### **Backend:**
- **FastAPI**: Handles requests for text summarization.
- **Hugging Face BART Model**: Utilized for generating text summaries.
- **PyTorch**: Framework used to load and use the pre-trained BART model.
- **CORS Middleware**: Configured to allow frontend applications to make requests to the backend.
- **GPU Support**: The application is optimized to leverage GPU for faster model inference using the NVIDIA container runtime.
- **Uvicorn**: ASGI server used to serve the FastAPI app, providing asynchronous handling of API requests for efficient performance.

### **Frontend:**
- **HTML & JavaScript**: Provides a simple user interface to input text, adjust summary length, and view results.
- **NGINX**: Used to serve static frontend files.

### **Docker**
- Docker is used to containerize both the backend and frontend, making it easy to deploy and scale the application.
  - **Backend**: Runs FastAPI with GPU support for faster inference using the BART model.
  - **Frontend**: Serves the HTML and JavaScript files through NGINX.

### **Docker Compose**
- A `docker-compose.yml` file is used to orchestrate the deployment of both backend and frontend services.

## **System Architecture**
The diagram below illustrates the architecture of the Text Summarizer:

![System Architecture Diagram](https://github.com/AzzedineNed/BART-Large-CNN-LLM-FastAPI-TextSummarizer-Deploy/blob/master/screenshots/Diagram.PNG)  
*System architecture illustrating the backend and frontend interaction, including GPU utilization for fast inference.*

## **Features**
- **Text Summarization**: Input text is summarized based on configurable minimum and maximum summary lengths.
- **Health Check Endpoint**: `/health` endpoint to check if the backend is ready.
- **Simple Web UI**: Users can interact with the summarizer via a clean, minimal frontend.
- **GPU Support**: Utilizes GPU for model inference, ensuring fast performance.
- **Uvicorn for Efficient API Handling**: Uvicorn is used to serve the FastAPI application, ensuring efficient handling of API requests.

### **Prerequisites**
- **Docker**: Make sure Docker is installed on your machine.
- **NVIDIA GPU**: Ensure you have NVIDIA GPU drivers installed, **CUDA Toolkit** and **NVIDIA Docker** runtime configured for optimal performance.

## **Installation**

To run the project locally or in a production environment, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AzzedineNed/BART-Large-CNN-LLM-FastAPI-TextSummarizer-Deploy.git
   cd BART-Large-CNN-LLM-FastAPI-TextSummarizer-Deploy
   ```
2. **Build the Docker containers**:
   Use Docker Compose to build and start both the frontend and backend services.
   ```bash
   docker-compose up --build
   ```
3. **Acces the Application**:
   - The frontend will be available on http://localhost:8080.
   - The backend (API) will be running at http://localhost:8000.

## **Endpoints**
**POST /summerize/**

This endpoint accepts a POST request with the following JSON payload:

```json
{
  "article": "string",
  "min_length": "int",
  "max_length": "int"
}
```
- **article**: The text to be summarized (required).
- **min_length**: The minimum length of the summary (default is 40).
- **max_length**: The maximum length of the summary (default is 150).

- The response will contain the summarized text
```json
 {
  "summary": "string"
}
```
**GET /health**

This endpoint checks the health of the backend. It returns:

```json
{
  "status": "ready"
}
```
This project demonstrates the deployment of a text summarization service using the BART model, FastAPI, and Docker. With a simple frontend for user interaction and GPU acceleration for efficient processing, it provides a scalable solution for text summarization.  

Feel free to explore, modify, and contribute to improve its functionality! 

   

   


