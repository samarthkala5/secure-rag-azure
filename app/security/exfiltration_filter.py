EXFILTRATION_ACTIONS = [
    "print",
    "show",
    "give",
    "provide",
    "dump",
    "export",
    "extract",
    "display",
    "reveal",
    "list",
    "reproduce",
    "output"
]

DOCUMENT_TARGETS = [
    "document",
    "documents",
    "policy",
    "policies",
    "page",
    "pages",
    "content",
    "contents",
    "text",
    "file",
    "files"
]


def detect_exfiltration_attempt(query):

    q = query.lower()

    action_found = any(
        action in q
        for action in EXFILTRATION_ACTIONS
    )

    target_found = any(
        target in q
        for target in DOCUMENT_TARGETS
    )

    return action_found and target_found