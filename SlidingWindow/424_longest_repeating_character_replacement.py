# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length

class Solution:
    def characterReplacement(self, s: str, num_moves: int) -> int:
        a = [0]*26
        left = 0
        ans = 0
        n = len(s)
        ord_A_unicode = ord('A')

        # sliding window approach
        for right in range(n):
            a[ord(s[right]) - ord_A_unicode] += 1
            max_freq = max(a)
            window_size = right - left + 1 

            # while we dont have a valid window and left is valid
            # window_size - max_freq = how many moves we need to make
            while window_size - max_freq > num_moves and left<n:
                # decrease the chars freq by 1 
                a[ord(s[left]) - ord_A_unicode] -= 1
                # move left over
                left += 1
                # compute new window size and max freq
                window_size = right - left + 1
                max_freq = max(a)

            # re check answer
            ans = max(window_size, ans)

        return ans


