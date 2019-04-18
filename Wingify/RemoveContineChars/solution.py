# The question is not much clear to me! Still recursively remove means if some 
# chars were deleted from main string, repeate process of deleting duplicate
# from new string as main string. If no chars deleted stop.

import itertools

def rdeldups(string):
    L = [ (c, sum(1 for _ in g)) for c, g in itertools.groupby(string) ]
    
    flag = True
    while flag and L:
        flag = False
        newL = []
        c, occurence = L[0]
        newL.append((c, occurence))
        for i in xrange(1, len(L)):
            nextc, occurence = L[i]
            if (occurence == 1) or (c > nextc):
                c = nextc
                newL.append((c, occurence))
                continue
            flag = True
        L = newL
    return "".join(c * occurence for c, occurence in L)
    
assert rdeldups("WIINGGIIFFFYYY") == "WIINGGFFF"
