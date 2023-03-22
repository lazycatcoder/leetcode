'''
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.


Constraints:
• -2**31 <= x <= 2**31 - 1


Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
'''

class Solution:
    def reverse(self, x):
        if x >= 0:
            result = int(str(x)[::-1])
        else:
            result = -int(str(abs(x))[::-1])
        if result < -2**31 or result > 2**31 - 1:
            return 0
        else:
            return result