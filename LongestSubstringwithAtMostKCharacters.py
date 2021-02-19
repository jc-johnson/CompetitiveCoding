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
        # left and right are pointers to navigate the given string - we can create an inner substring to analyze using 2 pointers 
        # count the number of distinct characters we've seen
        # count the max string length - setting max lower bound at 0 for max() comparison later
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

            # Once the number of distinct chars is greater than K
            # We start removing all instances of the left most character from the iterative substring and the hash map
            # There is no point in calculating more distinct numbers than k
            # We only keep track of k number of characters in our hash map

            # We have now seen more than k different characters - start iterating through the string with our left pointer 
            # Use our left pointer to remove the left most character from our substring 
            # We will be dropping one character from our substring so we can look at others 
            while num_distinct_chars > k: 
                # We are now creating a substring within the given string with our left pointer 
                map[string[left]] -= 1 # Decrement the counter for the left most char in our map until it reaches 0. Once the counter is 0, remove it from map.
                if map[string[left]] == 0:  # Remove this character from our map. We decremented it's count to equal 0 so we can remove it.
                    num_distinct_chars -= 1     # Number of distinct chars must change to reflect the char deletion from the map. 
                    del map[string[left]]
                left += 1       # Advance the left pointer of our substring

            # If the current window is greater than the max window, we update the max
            # maximum is updated every iteration
            # right pointer index - left pointer index + 1 since arrays and strings are 0 indexed  
            maximum = max(right - left + 1, maximum)
            right += 1 # Increment right pointer (main pointer)

        return maximum


def main():
    print("hello world!")
    s = Solution()
    ans = s.longestSubstringWithAtMostKDistinctCharacters("",2)
    print(ans)

    ans = s.longestSubstringWithAtMostKDistinctCharacters("f",2)
    print(ans)

    ans = s.longestSubstringWithAtMostKDistinctCharacters("coccccoffee",2)
    print(ans)

    ans = s.longestSubstringWithAtMostKDistinctCharacters("cccccoffee",2)
    print(ans)

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

    ans = s.longestSubstringWithAtMostKDistinctCharacters("ffpzskfff",2)
    print(ans)

    ans = s.longestSubstringWithAtMostKDistinctCharacters("ccooff",2)
    print(ans)

    ans = s.longestSubstringWithAtMostKDistinctCharacters("f",2)
    print(ans)

    ans = s.longestSubstringWithAtMostKDistinctCharacters("f",2)
    print(ans)

if __name__ == "__main__":
    main()        