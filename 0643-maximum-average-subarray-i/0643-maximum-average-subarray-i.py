class Solution:
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            if window_sum > max_sum:
                max_sum = window_sum

        return max_sum / float(k)

s = Solution()

print(s.findMaxAverage([1,12,-5,-6,50,3], 4))
print(s.findMaxAverage([5], 1))
