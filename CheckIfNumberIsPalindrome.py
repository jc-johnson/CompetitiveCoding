"""
A palindrome is a sequence that reads the same forwards and backward.

Given an integer as input, write a function that tests if it is a palindrome.

Note: A negative number cannot be a palindrome due to the - sign

Constraints: You may not cast the number to a string

Solution summary: We compare at the start and end of the number. If there is a mismatch in symmetry then the number is not a palindrome.
"""

import math

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x <= 0:
            return x == 0

        logarithm_answer = math.log10(x)                    # get the base 10 log of x
        total_digits = math.floor(logarithm_answer) + 1     # get total number of digits in given number 
        msd_mask = math.pow(10, total_digits - 1)           

        # Iterate through half of the strings 
        for i in range(int(total_digits) // 2):
            most_significant_digit = x // msd_mask
            ones_place_digit = x % 10

            if most_significant_digit != ones_place_digit:
                return False

            x %= msd_mask  # Remove most significant digit of x
            x //= 10  # Remove last significant digit of x

            msd_mask //= 100  # Remove 2 0's from the mask since we just removed 2 digits

        return True

def main():
    print("hello world!")
    s = Solution()
    ans = s.isPalindrome(22)
    print(ans)
    
if __name__ == "__main__":
    main()