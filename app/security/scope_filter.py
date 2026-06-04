ALLOWED_KEYWORDS = [
    "vpn",
    "remote access",
    "security",
    "policy",
    "authentication",
    "mfa",
    "access",
    "incident",
    "retention",
    "device",
    "classification",
    "compliance",
    "governance",
    "endpoint",
    "audit",
    "logging",
    "log",
    "monitoring",
    "response",
    "classification",
    "information",
    "instructions",
    "prompt",
    "system",
    "configuration"
]

def is_in_scope(query):

    q = query.lower()

    for keyword in ALLOWED_KEYWORDS:
        if keyword in q:
            return True

    return False