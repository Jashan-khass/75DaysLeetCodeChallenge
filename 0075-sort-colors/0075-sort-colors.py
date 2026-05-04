class Solution:
    def sortColors(self, nums):
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

def run_tests():
    test_cases = [
        ([2,0,2,1,1,0], [0,0,1,1,2,2]),
        ([2,0,1], [0,1,2])
    ]
    
    for nums, expected in test_cases:
        Solution().sortColors(nums)
        print(nums, nums == expected)

if __name__ == "__main__":
    run_tests()