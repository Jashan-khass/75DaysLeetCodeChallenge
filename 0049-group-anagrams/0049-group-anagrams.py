from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            groups[key].append(word)
        return list(groups.values())

s = Solution()

print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(s.groupAnagrams([""]))
print(s.groupAnagrams(["a"]))
print(s.groupAnagrams(["abc","bca","cab","xyz","zyx"]))
print(s.groupAnagrams(["listen","silent","enlist","google","gogole"]))