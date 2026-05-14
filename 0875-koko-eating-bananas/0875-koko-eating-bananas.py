class Solution:
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            hours = 0

            for pile in piles:
                hours += (pile + mid - 1) // mid

            if hours <= h:
                right = mid
            else:
                left = mid + 1

        return left


# Test Cases
sol = Solution()

print(sol.minEatingSpeed([3, 6, 7, 11], 8))      # 4
print(sol.minEatingSpeed([30, 11, 23, 4, 20], 5)) # 30
print(sol.minEatingSpeed([30, 11, 23, 4, 20], 6)) # 23