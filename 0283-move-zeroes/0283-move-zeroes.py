class Solution:
    def moveZeroes(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1


# ----------- Test Cases -----------

def run_tests():
    sol = Solution()
    
    cases = [
        [0, 1, 0, 3, 12],
        [0]
       
    ]
    
    for nums in cases:
        original = nums[:]
        sol.moveZeroes(nums)
        print("Input:", original, "-> Output:", nums)


# Run tests
run_tests()