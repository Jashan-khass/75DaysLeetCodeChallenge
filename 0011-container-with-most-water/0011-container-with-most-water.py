class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_water = 0
        
        while left < right:
            h = min(height[left], height[right])
            width = right - left
            max_water = max(max_water, h * width)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_water

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.maxArea([1,1]))
print(s.maxArea([4,3,2,1,4]))
print(s.maxArea([1,2,1]))
print(s.maxArea([2,3,10,5,7,8,9]))