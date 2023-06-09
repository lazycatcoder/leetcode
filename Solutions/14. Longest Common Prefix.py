'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
 

Constraints:
• 0 <= strs[i].length <= 200
• 1 <= strs.length <= 200
• strs[i] consists of only lowercase English letters.


Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        min_str = min(strs)
        max_str = max(strs)

        for i, char in enumerate(min_str):
            if char != max_str[i]:
                return min_str[:i]

        return min_str