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
"""

import sys

class Solution:
    def distanceOfClosestRepeatedEntries(self, sentence):
        '''
        :type sentence: list of str
        :rtype: int
        '''
        word_to_index_map = {}              # <Word, Index> 
        nearest_distance = sys.maxsize      # keep a global method variable for min/max comparison

        # simple string iteration
        for i in range(0, len(sentence)):
            word = sentence[i]

            # check our hash map to see if we've seen this word before 
            if word in word_to_index_map:
                # get the index where this word last appeared 
                last_appearance_index = word_to_index_map[word]
                # calculate distance between two appearances of the current word 
                current_nearest_distance = i - last_appearance_index

                # compare the recently calculated nearest distance with our global variable for nearest distance 
                nearest_distance = min(
                    nearest_distance,
                    current_nearest_distance
                )

            # We have not seen this word before. Add it and its index to the map.
            word_to_index_map[word] = i

        # return -1 if we never changed our global nearest distance variable 
        # else return the calculated nearest distance 
        return -1 if nearest_distance == sys.maxsize else nearest_distance