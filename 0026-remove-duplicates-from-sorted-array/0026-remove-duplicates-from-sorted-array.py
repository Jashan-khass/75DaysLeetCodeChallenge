class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        return k

# test cases
s = Solution()

nums1 = [1,1,2]
k1 = s.removeDuplicates(nums1)
print(k1, nums1[:k1])

nums2 = [0,0,1,1,1,2,2,3,3,4]
k2 = s.removeDuplicates(nums2)
print(k2, nums2[:k2])
