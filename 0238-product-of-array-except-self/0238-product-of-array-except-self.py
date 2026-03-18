class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1]*n
        left = 1
        for i in range(n):
            res[i] = left
            left *= nums[i]
        right = 1
        for i in range(n-1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res

s = Solution()
print(s.productExceptSelf([1,2,3,4]))
print(s.productExceptSelf([-1,1,0,-3,3]))