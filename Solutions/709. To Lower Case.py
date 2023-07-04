'''
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.


Constraints:
• 1 <= s.length <= 100
• s consists of printable ASCII characters.


Example 1:
Input: s = "Hello"
Output: "hello"

Example 2:
Input: s = "here"
Output: "here"

Example 3:
Input: s = "LOVELY"
Output: "lovely"
'''


class Solution:
    def toLowerCase(self, s: str) -> str:
        result = ""
        for char in s:
            if char.isupper():
                result += chr(ord(char) + 32)
            else:
                result += char
        return result