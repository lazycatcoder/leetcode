'''
Given an integer x, return true if x is a 
palindrome, and false otherwise.


Constraints:
• -2**31 <= x <= 2**31 - 1


Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''

class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        elif x == 0:
            return True
        x_str = str(x)
        if x_str == x_str[::-1]:
            return x