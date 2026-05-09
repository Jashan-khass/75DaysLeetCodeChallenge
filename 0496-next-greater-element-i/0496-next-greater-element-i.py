class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater = {}

        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)

        while stack:
            next_greater[stack.pop()] = -1

        return [next_greater[num] for num in nums1]


# Test Cases
sol = Solution()

print(sol.nextGreaterElement([4,1,2], [1,3,4,2]))
print(sol.nextGreaterElement([2,4], [1,2,3,4]))