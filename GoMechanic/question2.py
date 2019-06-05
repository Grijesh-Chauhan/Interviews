import itertools
try:
    from math import gcd
except ImportError:
    from fractions import gcd

# FIXME may be use limit to fix runtime for larger runway lenght!
Limit = 10 ** 9 + 7

def co_prime_pairs(n):
    for pair in itertools.product(range(1, n+1), range(1, n+1)):
        if gcd(*pair) == 1:
            yield pair
            
def co_primes(n):
    """ returns list of co-primes for 1 to n """
    pairs = tuple(co_prime_pairs(n))
    return [tuple(pair[1] for pair in pairs if pair[0] == i) for i in range(n+1)]

def ways(num, length):
    coprimes = co_primes(num)
    ways = [0] + [1] * num
    for _ in range(length):
        ways = [
            sum(map(ways.__getitem__, coprimes[i]))
            for i in range(num + 1)
        ]
    return ways[1] % Limit

if __name__ == '__main__':
    A = int(input("enter A, the runway length | 1 <= A <= 10\u2079: "))
    B = int(input("enter B, the number of runways | 0 <= B <= 10: "))
    
    assert 1 <= A <= 10 ** 9, "1 <= A <= 10\u2079"
    assert 1 <= B <= 10, "0 <= B <= 10"
    print (ways(B, A))
