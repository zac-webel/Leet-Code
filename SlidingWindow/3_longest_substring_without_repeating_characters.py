# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        ans = 0
        left = 0
        # sliding window approach
        for right, char in enumerate(s):
            # check if the current value is already in our window
            if char in seen and seen[char] >= left:
                # move left to it's last seen idx + 1 so the char is not double counted in our window
                left = seen[char] + 1
            
            # update the seen hashmap 
            seen[char] = right 
            
            # update the ans
            ans = max(ans, right - left + 1)

        return ans
    

# example
# 'bbbbb'

# starting state
# left = 0
# right = 1
# seen = {'b':0}

# update left 
# left = 1

# update seen 
# seen['b'] = 1

# update ans 
# ans = 1 - 1 + 1
