import re

def sanitize_input(prompt):
    """
    Remove potentially harmful or suspicious input.
    """
    # Example sanitization: remove excessive special characters
    sanitized = re.sub(r'[^\w\s.,?!-]', '', prompt)
    return sanitized.strip()

def validate_input(prompt):
    """
    Check for forbidden or suspicious content in the query.
    """
    forbidden_patterns = [
        r'(delete|drop|shutdown)',  # SQL-like commands
        r'(\bexec\b|\bcall\b)',     # Execution commands
        r'(system\(|os\.)',         # OS-level commands
        r'(--|;|#)',                # Comment/termination symbols
    ]
    for pattern in forbidden_patterns:
        if re.search(pattern, prompt, re.IGNORECASE):
            return False
    return True
