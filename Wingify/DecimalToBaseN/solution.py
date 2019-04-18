import string
from itertools import imap

def shiftBase(number, base):
    symbols = string.digits + string.ascii_letters + '_-'
    
    digits = []
    while number:
        quotient, remainder = divmod(number, base)
        digits.append(symbols[remainder])
        number = quotient
    return "".join(imap(str, reversed(digits)))





if __name__ == '__main__':
    assert shiftBase(15, 16) == 'f'
    assert shiftBase(16, 16) == '10'
    assert shiftBase(255, 16) == 'ff'
    assert shiftBase(63, 64) == '-'
    assert shiftBase(4095, 64) == '--'
    assert shiftBase(35, 36) == 'z'
    assert shiftBase(36, 36) == '10'
    assert shiftBase(8, 8) == '10'
    assert shiftBase(63, 8) == '77'
