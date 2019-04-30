"""
ConteryLink has array of string-numbers, may contain special numbers that is if a 
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

# I think i get the trick!!
# if a number is palindrome than that number should be special number!

def count_special(array):
    count = 0
    for snum in array:
        num = int(snum)
    for i in xrange(1, num):
        if int(str(i).strip('0')[::-1]) + i == num:
                count += 1
                break
    return count
    
# note: my code did not pass complexity wise!
# I think it can be improved by replaceing 
#   xrange(1, num)
# by 
#   xrange(1, num / 2 if num > 18 else num)
