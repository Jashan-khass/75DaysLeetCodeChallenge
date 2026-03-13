class Solution:
    def containsDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


# -------- Test Cases --------
sol = Solution()

# Case 1
nums1 = [1,2,3,1]
print(sol.containsDuplicate(nums1))   

# Case 2
nums2 = [1,2,3,4]
print(sol.containsDuplicate(nums2))   

# Case 3
nums3 = [1,1,1,3,3,4,3,2,4,2]
print(sol.containsDuplicate(nums3))   

# Case 4 (single element)
nums4 = [5]
print(sol.containsDuplicate(nums4))   

# Case 5 (negative numbers)
nums5 = [-1,-2,-3,-1]
print(sol.containsDuplicate(nums5))  
        