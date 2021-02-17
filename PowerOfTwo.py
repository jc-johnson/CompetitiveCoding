"""
Power of Two
Given a non-negative integer input, return true if input is a power of two. Return false otherwise.

Example #1:
Input: 4
Output: true
Explanation: The number 4 is a power of two.

Example #2:
Input: 17
Output: false
Explanation: The number 17 is not a power of two.

Constraints:  Your solution should run in O(1) time.

Thinking In Binary
Observe that the binary representation of a power of two contains exactly one bit turned on. 
For example, the first few powers of two are 1 (which is 1 in binary), 2 (which is 10 in binary), and 4 (which is 100 in binary). 
Thus, it suffices to check whether the provided integer has exactly one bit turned on.
 This can be done by verifying that the quantity x & (x - 1) equals zero. If x is a power of two, then x & (x - 1) equals zero since the binary representation of (x - 1) will have ones in the positions leading up to the only bit turned on in x (and zero everywhere else). Conversely, if x is a positive number that is not a power of two, then there are at least two positions turned on. Performing the logical AND operator on x with (x - 1) will produce a non-zero quantity since subtracting one will not turn off both bits. There is one special case: this verification will not detect that zero is not a power of two due to how negative numbers are represented using two's complement. Thus, we verify this case separately.
"""

class Solution:
    def powerOfTwo(self, input):
        '''
        :type input: int
        :rtype: bool
        '''
        return input > 0 and (input & (input - 1)) == 0