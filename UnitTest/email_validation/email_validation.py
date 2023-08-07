import re

VALID_PROVIDERS = ["yahoo", "gmail", "outlook"]

def validate_email(email):
    """
    Validates an email address based on specified rules.

    Args:
        email (str): The email address to be validated.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    # Check proper email format
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False

    # Check for spaces in the address
    if " " in email:
        return False

    # Extract the email provider
    _, provider = email.split("@")
    provider = provider.split(".")[0].lower()

    # Check if the provider is valid and not a disposable email provider
    if provider not in VALID_PROVIDERS:
        return False

    return True
