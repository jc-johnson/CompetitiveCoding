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

        for i in range(0, len(string)):
            currentCharacter = string[i]

            if (currentCharacter in self.open_to_close_map):  # Closing bracket
                if not stack:
                    return False  # No matching opening bracket

                correct_opening_tag = self.open_to_close_map[currentCharacter]
                if stack.pop() != correct_opening_tag:
                    return False
            else:  # Opening bracket - must be matched eventually
                stack.append(currentCharacter)

        return not stack
