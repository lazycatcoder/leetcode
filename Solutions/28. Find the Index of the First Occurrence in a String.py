'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.


Constraints:
• 1 <= haystack.length, needle.length <= 104
• haystack and needle consist of only lowercase English characters.


Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0

Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1

Explanation: "leeto" did not occur in "leetcode", so we return -1.
'''

class Solution:
    def strStr(self, haystack, needle):
        n = len(haystack)
        m = len(needle)
        if m == 0:  
            return 0
        i = 0
        j = 0
        while i < n and j < m:
            if haystack[i] == needle[j]:
                j += 1
            else:
                i -= j
                j = 0
            i += 1
        if j == m:
            return i - j
        else:
            return -1  