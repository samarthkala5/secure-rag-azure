import json
from datetime import datetime

LOG_FILE = "security.log"


def log_event(query, status, blocked_by=None):

    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "query": query,
        "status": status,
        "blocked_by": blocked_by
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")