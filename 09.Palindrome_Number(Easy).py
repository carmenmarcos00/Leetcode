class Solution(object):
    def isPalindrome(self, x):
        if x < 0:                                   # All negative numbers are not Palindrome
            return False              
            
        list_to_reverse = []                        # Number to a list
        for digit in str(x):
            list_to_reverse.append(digit)
        reverse = list_to_reverse[::-1]             # Reverse the list

        if (list_to_reverse == reverse):            # Compare the 2 lists (normal and reversed)
            return True
        else:
            return False
