from app.security.scope_filter import is_in_scope

queries = [
    "What is VPN timeout policy?",
    "What is the capital of France?",
    "Explain password requirements."
]

for q in queries:
    print(q)
    print(is_in_scope(q))
    print()