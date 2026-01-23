# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 

# Constraints:

# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1>n2: return False 

        count1, count2 = [0]*26, [0]*26

        ord_a_unicode_value = ord('a') # used to zero index our array
        for i in range(n1):
            count1[ord(s1[i]) - ord_a_unicode_value] += 1
            count2[ord(s2[i]) - ord_a_unicode_value] += 1
        
        if count1 == count2: return True

        for i in range(n1, n2):
            count2[ord(s2[i]) - ord_a_unicode_value] += 1
            count2[ord(s2[i-n1]) - ord_a_unicode_value] -= 1 # remove the first char in our window
            if count1 == count2:
                return True
        return False
