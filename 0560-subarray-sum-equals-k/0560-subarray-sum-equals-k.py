class Solution:
    def subarraySum(self, nums, k):
        prefix_sum = {0: 1}
        curr_sum = 0
        count = 0
        
        for num in nums:
            curr_sum += num
            if curr_sum - k in prefix_sum:
                count += prefix_sum[curr_sum - k]
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1
        
        return count

sol = Solution()
print(sol.subarraySum([1,1,1], 2))
print(sol.subarraySum([1,2,3], 3))