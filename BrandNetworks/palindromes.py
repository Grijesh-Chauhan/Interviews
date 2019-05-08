def is_palindrome(word):
    """
    Determines if the given word is a palindrome. Palindromes are spelled the
    same backwards and forwards. Palindromes must be at least 2 characters 
    long.
    
    For example: aa, aba, abba, abcba. 

    Args:
        word (str) - The word to be tested
    Returns:
        bool - True if the word is a palindrome

    """
    return len(word) >= 2 and word == word[::-1]
    
    
import re
_has_palindrome = re.compile(r"(?P<letter>\w)\w?(?P=letter)").search
def contains_palindrome(word):
    """
    Determines if the given word has a palindrome in it.
    
    Examples: abccd, abcdedfg, abcdefedgh.

    Args:
        word (str) - The word to be tested
    Returns:
        bool - True if the word contains a palindrome
    """
    return bool(_has_palindrome(word))

# https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/
# https://www.geeksforgeeks.org/?p=19155/
# https://www.geeksforgeeks.org/longest-palindromic-substring-set-2/
# https://www.geeksforgeeks.org/longest-palindromic-substring-using-palindromic-tree-set-3/
# https://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-2/
# https://www.geeksforgeeks.org/number-string-length-n-no-palindromic-sub-string/
# https://cp-algorithms.com/
# https://www.hackerrank.com/topics/manachers-algorithm

def find_longest_palindrome(word):
    """
    Finds the longest palindrome in the word. If none is found, returns the 
    empty string. 
    
    Examples: 
        abccd -> cc 
        abccdedfg -> ded
        abcdefedghcccc -> defed
    """
    start, maxlen = 0, 0
    def expand(low, high):
        nonlocal start, maxlen
        while 0 <= low and high < len(word) and word[low] == word[high]:
            if high - low + 1 > maxlen:
                start, maxlen = low, high - low + 1
            low -= 1
            high += 1
                
    for i in range(len(word)):
        expand(i, i+1)
        expand(i, i+2)
    return word[start: start + maxlen]

if __name__ == '__main__':
    for s, flag in (("aa", True),
                    ("1", False),
                    ("aba", True),
                    ("abcba", True),
                    ("ab", False),
                    ("狐狐", True),
                   ):
        assert is_palindrome(s) is flag, (s, flag)
        
    for s in 'aa', 'aba', 'abba', 'abcba':
        assert is_palindrome(s)

    for s, flag in (("aa", True),
                    ("1", False),
                    ("aba", True),
                    ("abcba", True),
                    ("ab", False),
                    ("狐狐", True),
                    ("1abxsda1", False),
                   ):
        assert contains_palindrome(s) is flag, (s, flag)

    for s in 'abccd', 'abcdedfg', 'abcdefedgh':
        assert contains_palindrome(s)
        
    for string, longest_palindrom in [  ("abccd", "cc"),
                                        ("abccdedfg", "ded"),
                                        ("abcdefedghcccc", "defed"),
                                        ("babcbabcbaccba", "abcbabcba"),
                                        ("caba", "aba"),
                                        ("abacdfgdcabba", "abba"),
                                        ("abacdedcaba", "abacdedcaba"),
                                     ]:
        assert find_longest_palindrome(string) == longest_palindrom
