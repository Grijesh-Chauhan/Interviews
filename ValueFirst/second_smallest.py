# Find second highest integer from a list of integers
# for second lowest check: https://stackoverflow.com/a/55492389/1673391

def second_highest(numbers):
    """ returns second highest or None 
        
        [1] => None
        [1, 1] => None
        [1, 2] => 1
    """
    if len(numbers) < 2:
        return None
    numbers = iter(numbers)
    first, second = next(numbers), next(numbers)
    if first < second:
        second, first = first, second
    for number in numbers:
        if number > first:
            first, second = number, first
        elif first > number > second:
            second = number
        elif number < second and first == second:
            second = number
    if first == second:
        return
    return second
    

if __name__ == '__main__':
    assert second_highest([0, 1, 2, 3, 4]) == 3
    assert second_highest([4, 3, 2, 1, 0]) == 3
    assert second_highest([1, 1, 1, 1, 1]) is None
    assert second_highest([1, 1, 1, 1, 2]) == 1
    assert second_highest([1, 1, 1, 1, 0]) == 0
    assert second_highest([1]) is None
    assert second_highest([]) is None
    assert second_highest([5, 5, 2, 2, 1, 1, 2.5 ]) == 2.5
    assert second_highest([5, 5, 2, 1, 3 ]) == 3
