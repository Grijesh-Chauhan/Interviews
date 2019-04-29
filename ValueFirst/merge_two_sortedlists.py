# my solution below is simple school level solution. far better solution avilable
# at https://stackoverflow.com/q/464342/1673391
#
# most intresting solutions is using heapq.merge
#  import heapq
#  list(heapq.merge(list1, list2))
#

def merge(list1, list2):
    """ list1 and list2 are asending order
        returns sorted(list1 + list2)
    """
    if not list1:
        return list2
    if not list2:
        return list1
    
    merged = []
    i1 = i2 = 0
    for _ in xrange(len(list1) + len(list2)):
        
        if i1 == len(list1):
            merged.extend(list2[i2:])
            break
            
        if i2 == len(list2):
            merged.extend(list1[i1:])
            break
            
        if list1[i1] < list2[i2]:
            merged.append(list1[i1])
            i1 += 1
        else:
            merged.append(list2[i2])
            i2 += 1
    
    return merged
            
if __name__ == '__main__':
    assert merge([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge([1, 2, 3], []) == [1, 2, 3]
    assert merge([], [4, 5, 6]) == [4, 5, 6]
    assert merge([1, 5], [4, 6, 7, 9, 10]) == [1, 4, 5, 6, 7, 9, 10]
    assert merge([1, 3, 5], [4, 6, 7, 9, 10]) == [1, 3, 4, 5, 6, 7, 9, 10]
