<<<<<<< HEAD
from fastapi import FastAPI
from pydantic import BaseModel
import re
import random

app = FastAPI(title="Agentic Honey-Pot API")

# ---------- Request Schema ----------
class MessageInput(BaseModel):
    message: str
    channel: str = "sms"

# ---------- Persona Templates ----------
CONFUSED_PERSONA = [
    "I don’t understand… what does this mean?",
    "Can you explain it clearly?",
    "Will my account stop working?"
]

WORRIED_PERSONA = [
    "Oh no 😟 I need my account urgently",
    "Please help me, what should I do now?",
    "I cannot afford to lose access"
]

SEMI_AWARE_PERSONA = [
    "Can you send official proof?",
    "Is there a website or number to verify?",
    "How do I know this is real?"
]

# ---------- Scam Keywords ----------
SCAM_KEYWORDS = [
    "kyc", "blocked", "verify", "urgent", "pay",
    "click", "link", "account", "upi", "bank"
]

# ---------- Entity Extraction ----------
def extract_entities(text):
    upi = re.findall(r"[a-zA-Z0-9.\-_]{2,}@[a-zA-Z]{2,}", text)
    phone = re.findall(r"\+91\d{10}", text)
    link = re.findall(r"https?://\S+", text)

    return {
        "upi_id": upi[0] if upi else None,
        "phone_number": phone[0] if phone else None,
        "phishing_link": link[0] if link else None
    }

# ---------- Main API ----------
@app.post("/analyze")
def analyze_message(data: MessageInput):
    message_lower = data.message.lower()

    # Scam confidence calculation
    keyword_hits = sum(1 for k in SCAM_KEYWORDS if k in message_lower)
    confidence = min(0.3 + keyword_hits * 0.15, 0.95)
    is_scam = confidence > 0.6

    # Persona selection (AGENTIC PART)
    persona_used = []
    if confidence < 0.7:
        response = random.choice(CONFUSED_PERSONA)
        persona_used.append("Confused Victim")
    elif confidence < 0.85:
        response = random.choice(WORRIED_PERSONA)
        persona_used.append("Worried Victim")
    else:
        response = random.choice(SEMI_AWARE_PERSONA)
        persona_used.append("Semi-Aware User")

    entities = extract_entities(data.message)

    return {
        "scam_detected": is_scam,
        "scam_type": "KYC Fraud" if is_scam else "Unknown",
        "confidence_score": round(confidence, 2),
        "persona_used": persona_used,
        "extracted_entities": entities,
        "risk_level": "HIGH" if confidence > 0.85 else "MEDIUM",
        "agent_response": response
    }
=======
from fastapi import FastAPI
from pydantic import BaseModel
import re
import random

app = FastAPI(title="Agentic Honey-Pot API")

# ---------- Request Schema ----------
class MessageInput(BaseModel):
    message: str
    channel: str = "sms"

# ---------- Persona Templates ----------
CONFUSED_PERSONA = [
    "I don’t understand… what does this mean?",
    "Can you explain it clearly?",
    "Will my account stop working?"
]

WORRIED_PERSONA = [
    "Oh no 😟 I need my account urgently",
    "Please help me, what should I do now?",
    "I cannot afford to lose access"
]

SEMI_AWARE_PERSONA = [
    "Can you send official proof?",
    "Is there a website or number to verify?",
    "How do I know this is real?"
]

# ---------- Scam Keywords ----------
SCAM_KEYWORDS = [
    "kyc", "blocked", "verify", "urgent", "pay",
    "click", "link", "account", "upi", "bank"
]

# ---------- Entity Extraction ----------
def extract_entities(text):
    upi = re.findall(r"[a-zA-Z0-9.\-_]{2,}@[a-zA-Z]{2,}", text)
    phone = re.findall(r"\+91\d{10}", text)
    link = re.findall(r"https?://\S+", text)

    return {
        "upi_id": upi[0] if upi else None,
        "phone_number": phone[0] if phone else None,
        "phishing_link": link[0] if link else None
    }

# ---------- Main API ----------
@app.post("/analyze")
def analyze_message(data: MessageInput):
    message_lower = data.message.lower()

    # Scam confidence calculation
    keyword_hits = sum(1 for k in SCAM_KEYWORDS if k in message_lower)
    confidence = min(0.3 + keyword_hits * 0.15, 0.95)
    is_scam = confidence > 0.6

    # Persona selection (AGENTIC PART)
    persona_used = []
    if confidence < 0.7:
        response = random.choice(CONFUSED_PERSONA)
        persona_used.append("Confused Victim")
    elif confidence < 0.85:
        response = random.choice(WORRIED_PERSONA)
        persona_used.append("Worried Victim")
    else:
        response = random.choice(SEMI_AWARE_PERSONA)
        persona_used.append("Semi-Aware User")

    entities = extract_entities(data.message)

    return {
        "scam_detected": is_scam,
        "scam_type": "KYC Fraud" if is_scam else "Unknown",
        "confidence_score": round(confidence, 2),
        "persona_used": persona_used,
        "extracted_entities": entities,
        "risk_level": "HIGH" if confidence > 0.85 else "MEDIUM",
        "agent_response": response
    }
>>>>>>> 5aa8f7bc03fd21b039b5f30fcd46fbe6aaab65b5
