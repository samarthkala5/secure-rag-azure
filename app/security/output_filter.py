import re

SECRET_PATTERNS = [

    # API key assignments
    r"api[_ -]?key\s*[:=]\s*\S+",

    # Password assignments
    r"password\s*[:=]\s*\S+",

    # Secret assignments
    r"secret[_ -]?key\s*[:=]\s*\S+",

    # Connection strings
    r"connection\s+string\s*[:=]\s*\S+",

    # AWS access keys
    r"AKIA[0-9A-Z]{16}",

    # Private keys
    r"-----BEGIN[\s\S]*PRIVATE KEY-----",

    # JWTs
    r"eyJ[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+",

    # SQL style connection strings
    r"server=.*database=.*",

]


def contains_sensitive_data(text):

    for pattern in SECRET_PATTERNS:

        if re.search(
            pattern,
            text,
            re.IGNORECASE
        ):
            return True

    return False