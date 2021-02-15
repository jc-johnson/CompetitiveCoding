import pytest

class Solution:
    ' class contructor '
    def __init__(self):
        ' map that keeps track of each symbol pair '
        ' for each symbol tells you the corresponding closing symbol  '
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
            if (currentCharacter in self.open_to_close_map):  # Closing bracket

                'check if stack is null'
                if not stack:
                    return False  # No matching opening bracket

                'get the paired closing tag from the dictionary for the current character'
                correct_opening_tag = self.open_to_close_map[currentCharacter]

                ''
                if stack.pop() != correct_opening_tag:
                    return False

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
    print(ans)
    test_isValid()

if __name__ == "__main__":
    main()
