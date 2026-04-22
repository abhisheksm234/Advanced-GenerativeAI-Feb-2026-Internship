def detect_intent(query):
    q = query.lower()

    if any(word in q for word in ["refund", "return", "policy"]):
        return "faq"
    elif any(word in q for word in ["complaint", "issue", "angry"]):
        return "escalate"
    elif any(word in q for word in ["human", "agent"]):
        return "human"
    else:
        return "general"