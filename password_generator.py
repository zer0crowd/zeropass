import random
import string

def generate_password(length=12):
    """Genera una contraseña segura con letras, números y símbolos."""
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(random.choice(chars) for _ in range(length))
    return password