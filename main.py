# main.py
from fastapi import FastAPI, HTTPException
from calculator import operations
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Calculator API is running"}

class CalculateRequest(BaseModel):
    a: float
    b: float
    operation: str

@app.post("/calculate")
def calculate(payload: CalculateRequest):
    try:
        result = operations(
            a=payload.a, 
            b=payload.b, 
            operation=payload.operation.lower()
        )
        return {
            "status": "success",
            "operation": payload.operation,
            "result": result
        }
    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err))
    
    