
'''
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Constraints:
• 1 <= s.length <= 104;
• s consists of only English letters and spaces ' ';
• There will be at least one word in s.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()[::-1]
        s1 = s.find(' ')
        if s1 == -1:
            return len(s)
        else:
            return s1