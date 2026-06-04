class Solution:
    def rob(self, nums):
        prev1 = 0
        prev2 = 0

        for num in nums:
            temp = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = temp

        return prev1


sol = Solution()

print(sol.rob([1, 2, 3, 1]))      
print(sol.rob([2, 7, 9, 3, 1]))   