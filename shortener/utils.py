from random import choice
from string import ascii_letters, digits

SIZE = 6
AVAIABLE_CHARS = ascii_letters + digits

def create_random_code(chars=AVAIABLE_CHARS, size=SIZE):
    result = "".join([choice(chars) for _ in range(size)])
    return result

