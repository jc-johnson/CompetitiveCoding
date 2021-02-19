"""
    Overview: Use dictionary indexed by closing characters. Push opening chars on stack as you traverse string. When you get a closing char, pop stack to make sure last entered 
    opening string matches. 
"""

import unittest

class Solution:
    ' class contructor '
    def __init__(self):
        ' map that keeps track of each symbol pair '
        ' for each symbol tells you the corresponding closing symbol  '
        ' note: dictionary is indexed by closing symbol '
        self.open_to_close_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

    def isValid(self, string):
        '''
        :type s: str
        :rtype: bool
        '''
        stack = []

        'iterate through given string'
        for i in range(0, len(string)):

            currentCharacter = string[i]

            'check if the current character has an entry in the map - if so get it''s paired closing character'
            'check if the current character is a closing character '
            if (currentCharacter in self.open_to_close_map):  # Closing bracket

                'check if stack is null'
                if not stack:
                    return False  # No matching opening bracket

                'get the paired closing tag from the dictionary for the current character'
                correct_opening_tag = self.open_to_close_map[currentCharacter]

                'check the last opening tag that was pushed on the stack'
                'if the current closing character does not match the last associated opening character the string is invalid'
                if stack.pop() != correct_opening_tag:
                    return False

            # current character is an opening character     
            # if the current character is not a closing character, push it on the stack
            else:  # Opening bracket - must be matched eventually
                stack.append(currentCharacter)

        return not stack

def test_isValid():
    s = Solution()
    ans = s.isValid("(())")
    assert ans == True

def main():
    print("hello world!")
    s = Solution()
    ans = s.isValid("(())")
    assertTrue(ans)
    print(ans)
    test_isValid()

if __name__ == "__main__":
    main()
