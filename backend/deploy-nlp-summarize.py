from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import BartTokenizer, BartForConditionalGeneration
import torch

class Config:
    DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
    MAX_TOKEN_LEN = 1024

config = Config()

# Load model
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn').to(config.DEVICE)
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')

app = FastAPI()

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (OK for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextInput(BaseModel):
    article: str
    max_length: int = 150
    min_length: int = 40

@app.post("/summarize/")
async def summarize_text(text_input: TextInput):
    inputs = tokenizer(
        text_input.article,
        return_tensors='pt',
        padding=True,
        truncation=True,
        max_length=config.MAX_TOKEN_LEN
    )

    with torch.no_grad():
        summary_ids = model.generate(
            inputs['input_ids'].to(config.DEVICE),
            attention_mask=inputs['attention_mask'].to(config.DEVICE),
            max_length=text_input.max_length,
            min_length=text_input.min_length,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True
        )

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return {"summary": summary}

# NEW: Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ready"}
