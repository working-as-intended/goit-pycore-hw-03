import re


# Нормалізує номер телефону до міжнародного формату.
def normalize_phone(phone_number):
    digits = re.sub(r"\D", "", phone_number)

    if phone_number.strip().startswith("+") or digits.startswith("380"):
        return "+" + digits

    return "+38" + digits
