import random


def code():
    """Helper function to create code"""
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    value = random.sample(letters, 1) + random.sample('0123456789', 2)
    code = ''.join(map(str, value))
    return code