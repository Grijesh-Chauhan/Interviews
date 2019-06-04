from question2 import CoPrimePairs
from collections import defaultdict   
class Old:
    # to understandold solution!

    def coPrimes(n):
        """ returns lists of all coprimes for 1 to n """
        choices = defaultdict(list)
        for pair in CoPrimePairs[n]:
            choices[pair[0]].append(pair[1])
            if pair[0] != pair[1]:
                choices[pair[1]].append(pair[0])
        return choices  
      
    def ways(num, length, coprimes):
        ways = [0] + [1] * num
        for _ in range(length):
            total = sum(ways)
            nextways = [0] * (num + 1)
            nextways[1] = total
            for i in range(2, num + 1):
                nextways[i] = sum(ways[coprime] for coprime in coprimes[i])
            ways = nextways
        return total % (10**9 + 7)
        
    print (ways(3, 4, coPrimes(3)))
    
