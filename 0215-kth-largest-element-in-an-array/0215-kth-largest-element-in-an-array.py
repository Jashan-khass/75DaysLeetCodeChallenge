import random

class Solution:
    def findKthLargest(self, nums, k):
        k = len(nums) - k

        def quickselect(left, right):
            pivot = nums[random.randint(left, right)]
            l, r = left, right

            while l <= r:
                while nums[l] < pivot:
                    l += 1
                while nums[r] > pivot:
                    r -= 1
                if l <= r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1

            if k <= r:
                return quickselect(left, r)
            if k >= l:
                return quickselect(l, right)
            return nums[k]

        return quickselect(0, len(nums) - 1)


s = Solution()

print(s.findKthLargest([3,2,1,5,6,4], 2))
print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))