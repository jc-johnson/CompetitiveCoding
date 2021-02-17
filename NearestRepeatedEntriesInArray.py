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
        word_to_index_last_seen_at = {}
        nearest_repeated_entry_distance = sys.maxsize

        for i in range(0, len(sentence)):
            word = sentence[i]

            if word in word_to_index_last_seen_at:
                last_appearance_index = word_to_index_last_seen_at[word]
                distance_to_last_appearance = i - last_appearance_index

                nearest_repeated_entry_distance = min(
                    nearest_repeated_entry_distance,
                    distance_to_last_appearance
                )

            word_to_index_last_seen_at[word] = i

        return -1 if nearest_repeated_entry_distance == sys.maxsize else nearest_repeated_entry_distance