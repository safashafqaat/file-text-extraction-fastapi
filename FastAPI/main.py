from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Literal
import os
import PyPDF2
import docx
from PIL import Image
import pytesseract

app = FastAPI(title="File Upload & Text Extraction API")

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


class ExtractedTextResponse(BaseModel):
    file_name: str
    file_type: Literal["pdf", "docx", "jpg", "jpeg", "png"]
    extracted_text: str


def extract_text_from_pdf(file_path: str) -> str:
    text = ""
    try:
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() or ""
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"PDF extraction failed: {e}")
    return text

def extract_text_from_docx(file_path: str) -> str:
    text = ""
    try:
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"DOCX extraction failed: {e}")
    return text

def extract_text_from_image(file_path: str) -> str:
    text = ""
    try:
        img = Image.open(file_path)
        text = pytesseract.image_to_string(img)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"OCR extraction failed: {e}")
    return text


@app.post("/extract-text", response_model=ExtractedTextResponse)
async def extract_text(file: UploadFile = File(...)):

    allowed_extensions = ["pdf", "docx", "jpg", "jpeg", "png"]
    file_ext = file.filename.split(".")[-1].lower()

    if file_ext not in allowed_extensions:
        raise HTTPException(status_code=400, detail=f"Unsupported file type: {file_ext}")

    contents = await file.read()
    if len(contents) > 10 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File too large. Max size is 10 MB.")

    temp_file_path = f"temp_{file.filename}"
    with open(temp_file_path, "wb") as f:
        f.write(contents)

    if file_ext == "pdf":
        text = extract_text_from_pdf(temp_file_path)
    elif file_ext == "docx":
        text = extract_text_from_docx(temp_file_path)
    else:  
        text = extract_text_from_image(temp_file_path)

    os.remove(temp_file_path)

    if not text.strip():
        text = "No readable text found."

    return ExtractedTextResponse(
        file_name=file.filename,
        file_type=file_ext,
        extracted_text=text
    )
