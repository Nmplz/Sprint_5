import random
import string


def generate_random_email(domain):
    name = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{name}{domain}"


def generate_randon_password():
    pwd = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=8))
    return pwd
