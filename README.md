<h1 align="center">AI-Powered File Text Extractor</h1>

A **high-performance FastAPI service** that extracts text from **PDFs, DOCX files, and images** using **OCR and document parsing techniques**, built for **practical AI/ML applications** and scalable real-world workflows.


## Overview

This project provides a **robust backend API** to automate text extraction from multiple file formats:

- **PDFs** using PyPDF2  
- **Word documents (.docx)** using python-docx  
- **Images (JPG, JPEG, PNG)** using Tesseract OCR  

The API is designed to handle **file validation, size limits, and error handling**, returning structured JSON responses for easy integration with other applications. Ideal for AI-powered document workflows, chatbots, or RAG (Retrieval-Augmented Generation) systems.


## Key Features

- Extract text from PDF and DOCX documents  
- Perform OCR on image files (JPG, JPEG, PNG)  
- Handles files up to **10 MB**  
- Returns structured JSON responses with file name, type, and extracted text  
- Interactive API documentation with **Swagger UI** at `/docs`  
- Modular, clean, and scalable architecture for easy integration  


## Tech Stack

- **Backend & API**: FastAPI, Uvicorn  
- **Text Extraction**: PyPDF2, python-docx  
- **OCR**: Pillow, pytesseract  
- **Data Handling**: JSON  
- **Development Tools**: Python 3.9+, virtual environments  


### Error Handling:

Invalid file type → Returns 400 Unsupported file type
File exceeds 10 MB → Returns 400 File too large
Extraction failure → Returns detailed error message

---
## Installation

### Prerequisites

- Python 3.9 or higher  
- Tesseract OCR installed  
  - **Windows**: Configure `pytesseract.pytesseract.tesseract_cmd` in `main.py`  
  - **Linux/Mac**: Ensure `tesseract` is available in system PATH  

### Setup

1. Clone the repository:

```bash
git clone https://github.com/<safashafqaat>/ai-file-text-extractor.git
cd ai-file-text-extractor

2. Create and activate a virtual environment:

python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / Mac
source .venv/bin/activate


3. Install dependencies:

pip install -r requirements.txt


4. Run the FastAPI server:

uvicorn main:app --reload
Open the interactive API docs: http://127.0.0.1:8000/docs

### API Usage
Endpoint: /extract-text (POST)

Request: Upload a file (PDF, DOCX, JPG, JPEG, PNG)

Response Example:

{
  "file_name": "example.pdf",
  "file_type": "pdf",
  "extracted_text": "This is the text extracted from the PDF file..."
}
