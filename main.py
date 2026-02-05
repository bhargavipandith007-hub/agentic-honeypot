from fastapi import FastAPI

app = FastAPI()

@app.api_route("/honeypot/analyze", methods=["GET", "POST"])
def honeypot():
    return {
        "status": "success",
        "reply": "I am confused. Can you explain why my account is blocked?"
    }
