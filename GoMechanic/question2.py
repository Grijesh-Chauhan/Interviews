from collections import defaultdict

CoPrimePairs = {
    0: [],
    1: [(1, 1)],
    2: [(1, 1), (1, 2)],
    3: [(1, 1), (1, 2), (1, 3), (2, 3)],
    4: [(1, 1), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)],
    5: [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 5), (3, 4), (3, 5)],
    6: [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
        (2, 3), (2, 5),
        (3, 4), (3, 5),
        (5, 6),
       ],
    7: [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
        (2, 3), (2, 5), (2, 7),
        (3, 4), (3, 5), (3, 7),
        (4, 7),
        (5, 6), (5, 7),
        (6, 7),
       ],
    8: [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8),
        (2, 3), (2, 5), (2, 7),
        (3, 4), (3, 5), (3, 7), (3, 8),
        (4, 7),
        (5, 6), (5, 7), (5, 8),
        (6, 7),
        (7, 8),
       ],
    9: [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9),
        (2, 3), (2, 5), (2, 7), (2, 9),
        (3, 4), (3, 5), (3, 7), (3, 8),
        (4, 7), (4, 9),
        (5, 6), (5, 7), (5, 8), (5, 9),
        (6, 7),
        (7, 8), (7, 9),
        (8, 9),
       ],
    10: [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), 
        (1, 10),
        (2, 3), (2, 5), (2, 7), (2, 9),
        (3, 4), (3, 5), (3, 7), (3, 8), (3, 10),
        (4, 7), (4, 9),
        (5, 6), (5, 7), (5, 8), (5, 9),
        (6, 7),
        (7, 8), (7, 9), (7, 10),
        (8, 9),
        (9, 10),
       ],
}



    
def coprimes(n):
    """ returns lists of all coprimes for 1 to n """
    choices = defaultdict(list)
    for pair in CoPrimePairs[n]:
        choices[pair[0]].append(pair[1])
        if pair[0] != pair[1]:
            choices[pair[1]].append(pair[0])
    return choices
    
def coPrimes(n):
    """ coPrimes(n) == coprimes(n) """
    # iterating over tuple of tuples would be faster than dict of lists
    pairs = set()
    for pair in CoPrimePairs[n]:
        pairs.add(pair)
        pairs.add(pair[::-1])
    return tuple(
            tuple(pair[1] for pair in pairs if pair[0] == i)
            for i in range(n+1)
           )
   
if __name__ == '__main__':
    A = int(input("enter A, the runway length | 1 <= A <= 10\u2079: "))
    B = int(input("enter B, the number of runways | 0 <= B <= 10: "))
    
    assert 1 <= A <= 10 ** 9, "1 <= A <= 10\u2079"
    assert 1 <= B <= 10, "0 <= B <= 10"
    
    Limit = 10 ** 9 + 7
    num = B
    length = A
    
    coprimes = coPrimes(num)
    ways = [0] + [1] * num
    for _ in range(length):
        total = sum(ways)
        nextways = [0] * (num + 1)
        nextways[1] = total
        for i in range(2, num + 1):
            nextways[i] = sum(map(ways.__getitem__, coprimes[i]))
        ways = nextways
        
    print (total % Limit)
