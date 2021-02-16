"""
Longest Palindrome Construction
Given a string, determine the length of the longest possible palindromic string that can be constructed using the characters of the string. 

Example 1:
Input: "aabbc"
Output: 5 
Explanation: The longest palindromes possible are {"abcba", "bacab"}

Example 2:
Input: "abbcccd"
Output: 5
Explanation: The original string length is 7, but the longest palindromes are {"cbcbc",  "bcccb"}; 'a' and 'd' were not used.

Example 3:
Input: "aA"
Output: 1
Explanation: since the input is case-sensitive; the longest palindromes are {"a", "A"}

Example 4:
Input: "xyz"
Output: 1

Example 5:
Input: "ccc"
Output: 3
"""

'With Set'
'We use a set to manually track matches.'

class Solution:
    def longestPalindrome(self, s):
        '''
        :type s: str
        :rtype: int
        '''
        matchings = 0
        unmatched_characters = set()

        'Iterate through each character in a string' 
        for c in s:
            if c in unmatched_characters:
                unmatched_characters.remove(c)
                matchings += 1
            else:
                unmatched_characters.add(c)

        longest_palindrome_length = matchings * 2
        if len(unmatched_characters) != 0:
            longest_palindrome_length += 1

        return longest_palindrome_length