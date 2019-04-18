import re
import itertools     
import string

uppers = string.uppercase
def index(c):
    """returns index of a `c` in `uppers`"""
    return ord(c) - ord('A')
                
# probably do not need `_itergroups` use `groups` instead
_itergroups = re.compile(r"(?P<char>[A-Z])(?P<occurence>[0-9]*)").finditer
def groups(string):
    for m in _itergroups(string):
        yield m.group('char'), int(m.group('occurence') or 1)

def encode(string):
    encodes = []
    for k, g in itertools.groupby(string):
        occurence = sum(1 for _ in g)
        new_index = (index(k) + occurence) % 26
        chars = uppers[new_index]
        if occurence > 1:
            chars += str(occurence)        
        encodes.append(chars)
    return "".join(encodes)
                
def decode(string):
     decodeds = []
     for c, occurence in groups(string):
        if index(c) < occurence:
            chars = uppers[26 - occurence + index(c)]
        else:
            chars = uppers[index(c) - occurence]
        decodeds.append(chars * occurence)
     return "".join(decodeds)

assert encode("WIINNNGGIIFFFFFFFYYYY") == "XK2Q3I2K2M7C4"
assert decode("XK2Q3I2K2M7C4") == "WIINNNGGIIFFFFFFFYYYY"
