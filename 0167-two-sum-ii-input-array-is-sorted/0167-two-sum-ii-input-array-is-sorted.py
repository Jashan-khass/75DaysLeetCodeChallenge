class Solution(object):
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        
        while left < right:
            s = numbers[left] + numbers[right]
            
            if s == target:
                return [left + 1, right + 1]
            elif s < target:
                left += 1
            else:
                right -= 1


# Test cases
obj = Solution()

print(obj.twoSum([2, 7, 11, 15], 9))   # [1, 2]
print(obj.twoSum([2, 3, 4], 6))        # [1, 3]
print(obj.twoSum([-1, 0], -1))         # [1, 2]