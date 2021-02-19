"""

Given a string s, find the length of the longest substring that contains at most k distinct characters.

Example #1:
Input: s = "coffee", k = 2
Output: 4
Explanation: The substring "ffee" has length four, and it has only two distinct characters. No better (longer) solution exists.

Maintaining Character Count
We can traverse our string using two pointers: a left pointer, and a right pointer. 
Together, these pointers represent the current substring that we are considering. 

Furthermore, we can keep a hashmap to store the frequency of each character in our substring. 

On each step, we try to extend our substring by moving our right pointer forwards. 
   
As we move our right pointer forward, we can check whether or not our substring already contains 
the new character being processed at our right pointer by checking whether or not its frequency 
in our hashmap is equal to zero. If so, this character does not contribute anything to our distinct characters count.

Conversely, if the character is not already in our hashmap, then it is a distinct character, and we must increment our counter.
If our count of distinct characters ever exceeds k, then we must move the left pointer forward to evict some of the characters of our substring. 

While moving the left pointer forward, we decrement the frequency of the character being evicted. 
If the frequency of a character ever reaches zero, then we can decrement our counter.

While traversing our string, we take the maximal length over all valid strings to be our answer. 
This is computed on-the-fly. 

The overall runtime of this algorithm is O(N) where N is the length of our string 
 since we visit each character at most twice (once by the left pointer and once by the right pointer).

"""

class Solution:
    def longestSubstringWithAtMostKDistinctCharacters(self, string, k):
        '''
        :type s: str
        :type k: int
        :rtype: int
        '''
        # Initializes the table for mapping characters to occurences
        map = {}
        # left and right are pointers to navigate the given string 
        # setting max lower bound at 0 for max() comparison later
        # count the number of distinct characters we've seen
        # count the max string length
        left, right, num_distinct_chars, maximum = 0, 0, 0, 0
        
        # Simple iteration through a string - We will utilize a left and right pointer to traverse our string
        while right < len(string):
            # Check if char in map - Check if char at the right pointer is in the map 
            if string[right] in map:
                # If the entry exists increment the counter for it 
                map[string[right]] += 1
            # Current char is not in the map 
            else:
                # Initialize the counter in the map for this char -- we've now seen it once 
                map[string[right]] = 1
                num_distinct_chars += 1 # Increment the total number of distinct characters seen so far also 

            # If number of distinct characters is greater than k
            # We have seen more than k different characters 
            # If our distinct character counter exceeds k, then we move the left pointer forward until we are within our bound
            while num_distinct_chars > k:
                # Decrement the counter for the char our left pointer is referencing 
                map[string[left]] -= 1
                # This char isn't relevant to our final solution. 
                # There is not enough instances of this character to be valid for our final answer. 
                # We need at least k repeating characters. 
                if map[string[left]] == 0:  # Remove this number from our map. We decremented it's count to equal 0 so we can remove it.
                    num_distinct_chars -= 1 # Number of distinct chars must change to reflect the char deletion from the map. 
                    del map[string[left]]
                left += 1       # Advance the left pointer 

            # If the current window is greater than the max window, we update the max
            maximum = max(right - left + 1, maximum)
            right += 1 # Increment right pointer (main pointer)

        return maximum


def main():
    print("hello world!")
    s = Solution()
    ans = s.longestSubstringWithAtMostKDistinctCharacters("coffee",2)
    print(ans)

    ans = s.longestSubstringWithAtMostKDistinctCharacters("cofffee",2)
    print(ans)

    ans = s.longestSubstringWithAtMostKDistinctCharacters("f",2)
    print(ans)

    ans = s.longestSubstringWithAtMostKDistinctCharacters("ff",2)
    print(ans)

    ans = s.longestSubstringWithAtMostKDistinctCharacters("fffee",2)
    print(ans)

    ans = s.longestSubstringWithAtMostKDistinctCharacters("",2)
    print(ans)

    ans = s.longestSubstringWithAtMostKDistinctCharacters("zazazaf",2)
    print(ans)

    ans = s.longestSubstringWithAtMostKDistinctCharacters("ppf",2)
    print(ans)

    ans = s.longestSubstringWithAtMostKDistinctCharacters("f",2)
    print(ans)

    ans = s.longestSubstringWithAtMostKDistinctCharacters("f",2)
    print(ans)

    ans = s.longestSubstringWithAtMostKDistinctCharacters("f",2)
    print(ans)

    ans = s.longestSubstringWithAtMostKDistinctCharacters("f",2)
    print(ans)




if __name__ == "__main__":
    main()        