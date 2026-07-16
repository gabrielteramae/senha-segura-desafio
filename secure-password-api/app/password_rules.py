import re

MIN_LENGTH = 8

RULES = {
    "min_length": lambda pwd: len(pwd) >= MIN_LENGTH,
    "has_uppercase": lambda pwd: bool(re.search(r"[A-Z]", pwd)),
    "has_lowercase": lambda pwd: bool(re.search(r"[a-z]", pwd)),
    "has_digit": lambda pwd: bool(re.search(r"\d", pwd)),
    "has_special_char": lambda pwd: bool(re.search(r"[^A-Za-z0-9]", pwd)),
}

ERROR_MESSAGES = {
    "min_length": f"A senha deve possuir pelo menos {MIN_LENGTH} caracteres",
    "has_uppercase": "A senha deve conter pelo menos uma letra maiuscula",
    "has_lowercase": "A senha deve conter pelo menos uma letra minuscula",
    "has_digit": "A senha deve conter pelo menos um digito numerico",
    "has_special_char": "A senha deve conter pelo menos um caractere especial",
}


def validate_password(password: str) -> list[str]:
    failed_rules = [
        rule_name for rule_name, check in RULES.items() if not check(password)
    ]
    return [ERROR_MESSAGES[rule_name] for rule_name in failed_rules]
