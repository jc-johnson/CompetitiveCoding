"""
Define main
"""

def main():
    print("hello world!")
    s = Solution()
    ans = s.isValid("(())")
    print(ans)
    
if __name__ == "__main__":
    main()

"""
Iterate through words in sentence 


Example 1: Iterate over words of String
In this example, we will iterate over the words of a string and print them one by one.
"""

str = 'Hello! I am Robot. This is a Python example.'

#split string
splits = str.split()

#for loop to iterate over words array
for split in splits:
	print(split)

"""
Example 2: Clean String & Iterate Over Words of String
In this example, we will clean the string and remove anything other than alphabets and spaces. Then we split the string and iterate over the words.
"""
import re

str = 'Hello! I am Robot. This is a Python example.'

#clean string
pat = re.compile(r'[^a-zA-Z ]+')
str = re.sub(pat, '', str).lower()

#split string
splits = str.split()

#for loop to iterate over words array
for split in splits:
	print(split)