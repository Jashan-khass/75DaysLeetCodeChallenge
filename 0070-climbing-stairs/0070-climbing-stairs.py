class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n

        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b

        return b


sol = Solution()

test_cases = [2, 3]

for n in test_cases:
    print("n =", n, "ways =", sol.climbStairs(n))