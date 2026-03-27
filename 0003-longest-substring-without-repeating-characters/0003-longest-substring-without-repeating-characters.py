class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            if right - left + 1 > max_length:
                max_length = right - left + 1
        
        return max_length


sol = Solution()

test_cases = [
    "abcabcbb",
    "bbbbb",
    "pwwkew",
    "",
    "abcdef",
    "abba"
]

for s in test_cases:
    print("Input:", s, "Output:", sol.lengthOfLongestSubstring(s))