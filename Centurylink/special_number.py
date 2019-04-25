"""
ConteryLink has array of number strings, with a special number that is if number
is equals to a sum of a number and its reverse.

The objective is to count number of special numbers in the array.

Note: when you reverse a number prefex zeros can be removed  eg. 2300 -> 23

examples:

array = [22, 121]

answer: 2
explanation: 22 is equals to 11, and 121 is sum of 29 + 92

array = [12, 3]
answer: 1
explanation: 12 is sum of 6 + 6
"""

def count_special(array):
    count = 0
    for snum in array:
        num = int(snum)
        for i in xrange(1, num):
            if int(str(i).strip('0')[::-1]) + i == num:
                count += 1
                break
    return count
    
    
# note: my code does not pass complexity wise! and got rejected.
# If think we can improve code `xrange(1, num)` by `xrange(1, num)`
# for num > 18
