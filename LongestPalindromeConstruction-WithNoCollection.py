"""
Longest Palindrome Construction
Given a string, determine the length of the longest possible palindromic string that can be constructed using the characters of the string. 

Example 1:
Input: "aabbc"
Output: 5 
Explanation: The longest palindromes possible are {"abcba", "bacab"}

Example 2:
Input: "abbcccd"
Output: 5
Explanation: The original string length is 7, but the longest palindromes are {"cbcbc",  "bcccb"}; 'a' and 'd' were not used.

Example 3:
Input: "aA"
Output: 1
Explanation: since the input is case-sensitive; the longest palindromes are {"a", "A"}

Example 4:
Input: "xyz"
Output: 1

Example 5:
Input: "ccc"
Output: 3

"""

'Mine is similar but I didn''t use collections to maintain frequencies.'

class Solution {
public int longestPalindrome(String s) {
if(s == null || s.length() == 0) return 0;

int maxPalLen = 0;
int maxOddFreqLen = 0;
int[] freq = new int[256];

for(int i = 0; i < s.length(); i++){
char c = s.charAt(i);
freq[c]++;
}

for(int i = 0; i < freq.length; i++){
if(freq[i] > 0 ) {
if(freq[i] % 2 == 0){
maxPalLen += freq[i];
} else {
maxOddFreqLen = Math.max(maxOddFreqLen, freq[i]);
}
}
}
maxPalLen += maxOddFreqLen;

return maxPalLen;
}
}