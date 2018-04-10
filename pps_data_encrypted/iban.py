import string
import itertools

_LETTERS = itertools.chain(enumerate(string.digits + string.ascii_uppercase),
                 enumerate(string.ascii_lowercase, 10))
LETTERS = {ord(d): str(i) for i, d in _LETTERS}

def _number_iban(iban):
    return (iban[4:] + iban[:4]).translate(LETTERS)

def is_valid_iban(candidate_iban):
    return int(_number_iban(candidate_iban)) % 97 == 1
