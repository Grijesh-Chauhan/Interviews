"""
Given an array of positive and negative numbers, find if there is a zero_sum_subseqeunce 
(of size at-least one) with 0 sum.

Hind:
If the sum of a sub-sequence is zero then this implies that cumulative sum until
the start of the sub-sequence and end of the sub-sequence is same. For example 
sum of sub-sequence 3 to 5 = 0

Index:  0  1  3   4  5  6
       [2, 2, 2, -3, 1, 6]
           ^  ^      ^
           |  <--0-->|           
        <->|         |
 total:    4         |
        <---(4 + 0)->|
                     4
"""

def zero_sum_subseqeunce(array):
    if not array  or array[0] == 0:
        return []
    accumulate, total = {}, 0
    for index, number in enumerate(array):
        total += number
        if total in accumulate:
            start, end = accumulate[total] + 1, index
            return array[start: end+1]
        accumulate[total] = index
    return []        

if __name__ == '__main__':
    print (zero_sum_subseqeunce([0]))
    print (zero_sum_subseqeunce([]))
    print (zero_sum_subseqeunce([2, 2, 2, -3, 1, 6]))
    print (zero_sum_subseqeunce([4, 2, -3, 1, 6]))
    print (zero_sum_subseqeunce([4, 2, 0, 1, 6]))
    print (zero_sum_subseqeunce([-3, 2, 3, 1, 6]))
