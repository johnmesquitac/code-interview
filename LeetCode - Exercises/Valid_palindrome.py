''''
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
    Given a string s, return true if it is a palindrome, or false otherwise.

    #Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

    #Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

'''

def check_palindrome(s):
    text = ''.join([lower(char) for char in s if char.isalnum()])
    i = 0
    j = len(text)
    while i<j:
        if text[i]!=text[j]:
            return False
        i+=1
        j-=1
    return True
