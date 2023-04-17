'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

Constraints:
• 1 <= digits.length <= 100
• 0 <= digits[i] <= 9
• digits does not contain any leading 0's.


Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]

Example 3:
Input: digits = [9]
Output: [1,0]
'''


class Solution:
    def plusOne(self, digits):
        dig = ""
        for d in digits:
            dig += str(d)
        num = int(dig)
        num += 1
        num_str = str(num)
        res = []
        for d in num_str:
            res.append(int(d))
        return res