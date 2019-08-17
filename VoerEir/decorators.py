"""
toy decorators
"""
import functools

# asked decorator method to print...
def starify(print_or_return='print'):
    def decorator(sum):
        @functools.wraps(sum)
        def decorated_sum(a, b):
            ab = sum(a, b)
            string = "{} {} {}".format("*" * ab, ab, ab + len(str(ab)))
            if print_or_return == 'return':
                return string
            print(string)
        return decorated_sum
    return decorator
    
# abusing builtin name
@starify(print_or_return='return')
def sum(a, b: int) -> int:
    """
    >> sum(1, 2)
    3
    >> sum(10, 12)
    24
    >> sum(0, -1)
    -1
    >> sum(0, 0)
    0
    """
    return a + b
