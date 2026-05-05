class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        n = len(nums)
        
        for i in range(n - 2):
            left, right = i + 1, n - 1
            
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                
                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum
                
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    return curr_sum
        
        return closest


if __name__ == "__main__":
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4], 1))
    print(s.threeSumClosest([0, 0, 0], 1))