from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "API is running"}

@app.post("/analyze")
def analyze(data: dict):
    message = data.get("message", "")
    return {
        "received_message": message,
        "scam_detected": "kyc" in message.lower()
    }