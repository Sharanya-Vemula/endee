import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI
from pydantic import BaseModel
from backend.debug_engine import analyze_error

app = FastAPI()

class DebugRequest(BaseModel):
    error: str
    code: str

@app.get("/")
def home():
    return {"message": "Server running"}

@app.post("/debug")
def debug(req: DebugRequest):
    return analyze_error(req.error, req.code)