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

"""
With Hashtable
We count character frequencies and then determine the longest constructible palindrome from that information.
"""

class Solution:
    def longestPalindrome(self, s):
        '''
        :type s: str
        :rtype: int
        '''
        longest_palindrome_length = 0

        character_to_count = {}
        for c in s:
            if (not (c in character_to_count)):
                character_to_count[c] = 1
            else:
                character_to_count[c] = character_to_count[c] + 1

        most_frequent_odd_character = None
        most_frequent_odd_character_frequency = 0
        for c in character_to_count:
            count = character_to_count[c]

            if count % 2 == 0:
                longest_palindrome_length += count
            elif count > most_frequent_odd_character_frequency:
                most_frequent_odd_character = c
                most_frequent_odd_character_frequency = count

        longest_palindrome_length += most_frequent_odd_character_frequency

        if most_frequent_odd_character:
            character_to_count.pop(most_frequent_odd_character, None)

            for c in character_to_count:
                count = character_to_count[c]

                if count % 2 != 0:
                    longest_palindrome_length += count - 1

        return longest_palindrome_length