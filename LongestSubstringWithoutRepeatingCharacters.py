"""
Longest Substring without Repeating Characters
Given a string s, return the length of the longest substring of s without repeating characters.

Example 1:
Input: : "ABCABADEC"
Output: 5
Explanation: Though there are substrings such as "AB" and "ABC" that have all unique characters, "BADEC" is the longest unique character substring.

Example 2:
Input: : ""
Output: 0

Constraints:
All letters will be uppercase A-Z

Checking All Substrings
We can check all substrings and check if each substring has unique characters. We return the length of the longest unique character substring over all substrings.
"""

class Solution:
    def longestUniqueCharacterSubstring(self, string):
        '''
        :type s: str
        :rtype: int
        '''
        mapping = {}
        start = 0
        end = 0
        so_far = 0

        while end < len(string):
            if string[end] in mapping and mapping[string[end]] >= start:
                start = mapping[string[end]] + 1
            mapping[string[end]] = end

            so_far = max(so_far, end - start + 1)
            end += 1

        return so_far



"""
Two Pointers
We can use a left and right pointer to advance, as we go we can expand our "window" as the string stays unique and contract it when the property is broken.

"""

class Solution2:
    def longestUniqueCharacterSubstring(self, string):
        '''
        :type s: str
        :rtype: int
        '''
        mapping = {}
        start = 0
        end = 0
        so_far = 0

        while end < len(string):
            if string[end] in mapping and mapping[string[end]] >= start:
                start = mapping[string[end]] + 1
            mapping[string[end]] = end

            so_far = max(so_far, end + 1 - start)
            end += 1

        return so_far