"""
CenturyLink has array of string-numbers, may contain special numbers that is if a 
number is equals to a sum of a number and its reverse.

The objective is to count number of special numbers present in the array.

Note: when you reverse a number prefex zeros can be removed  eg. 2300 -> 23

example-1:

array = [22, 121]
answer: 2
explanation: 22 is equal to 11 + 11, and 121 is sum of 29 + 92

example-2:

array = [12, 3]
answer: 1
explanation: 12 is sum of 6 + 6
"""

def count_special(array):
    fewspecials = frozenset(str(i * 2) for i in xrange(10)) # single digits 
    count = 0
    for snum in array:
        if snum in fewspecials:
            count += 1
            continue
        elif len(snum) > 1 and snum == snum[::-1]: # palindrome numbers are those special numbers
            count += 1
    return count
  

# my actual submission was folowing, that did not pass complexities wise :(
# def is_special(snum):
#     num = int(snum)
#     for i in xrange(1, num):
#         if int(str(i).strip('0')[::-1]) + i == num:
#                 return True
#     return False
