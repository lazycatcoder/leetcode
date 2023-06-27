'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".


Constraints:
• The given address is a valid IPv4 address.


Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
'''


class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged_address = ""
        for char in address:
            if char == ".":
                defanged_address += "[.]"
            else:
                defanged_address += char
        return defanged_address