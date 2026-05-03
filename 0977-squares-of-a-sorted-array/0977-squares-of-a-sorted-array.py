class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pos = n - 1
        
        while left <= right:
            left_sq = nums[left] * nums[left]
            right_sq = nums[right] * nums[right]
            if left_sq > right_sq:
                result[pos] = left_sq
                left += 1
            else:
                result[pos] = right_sq
                right -= 1
            pos -= 1
        
        return result
s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))  # [0,1,9,16,100]
print(s.sortedSquares([-7,-3,2,3,11]))  # [4,9,9,49,121]