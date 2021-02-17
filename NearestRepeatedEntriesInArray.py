"""
Nearest Repeated Entries In An Array
Given an array words of words return the distance between the nearest repeated entries.

If no entry is repeated return -1.

Example 1:
Input:
[
  "This",
  "is",
  "a",
  "sentence",
  "with",
  "is",
  "repeated",
  "then",
  "repeated"
]
Output: 2
Explanation: "repeated" (index 6) and "repeated" (index 8) are 2 positions away.

Example 2:
Input:
[
  "This",
  "is",
  "a"
]
Output: -1
Explanation: There are no repeated entries.

Remember The Recent Index
We keep track of the most recent index that every word we have seen has occurred. We leverage this information to know the best answer at each word we inspect.

"""

import sys


class Solution:
    def distanceOfClosestRepeatedEntries(self, sentence):
        '''
        :type sentence: list of str
        :rtype: int
        '''
        word_to_index_hash_table = {}                       # keep hashmap for each word and its index <string word, int index>
        nearest_repeated_entry_distance = sys.maxsize       # initialize variable 

        split_String = sentence.split() # split string 

        # iterate through each word in given sentence 
        for i in range(0, len(split_String)):
            word = split_String[i]

            # check our hashtable to see if we've seen the current word before 
            if word in word_to_index_hash_table:

                # get the last index where the current word appeared
                last_appearance_index = word_to_index_hash_table[word]

                # subtract the last_appearance_index from current index to get distance 
                distance_to_last_appearance = i - last_appearance_index

                # is this needed? 
                nearest_repeated_entry_distance = min(
                    nearest_repeated_entry_distance,
                    distance_to_last_appearance
                )
            # update our hashtable with the current word and the current index
            word_to_index_hash_table[word] = i

        return -1 if nearest_repeated_entry_distance == sys.maxsize else nearest_repeated_entry_distance

def main():
    print("hello world!")
    s = Solution()
    ans = s.distanceOfClosestRepeatedEntries("This is is my car")
    print(ans)
    
if __name__ == "__main__":
    main()