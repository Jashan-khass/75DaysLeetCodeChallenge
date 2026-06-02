class Solution:
    def minCostClimbingStairs(self, cost):
        dp0 = cost[0]
        dp1 = cost[1]

        for i in range(2, len(cost)):
            dp0, dp1 = dp1, cost[i] + min(dp0, dp1)

        return min(dp0, dp1)


test_cases = [
    ([10, 15, 20], 15),
    ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6)
]

sol = Solution()

for cost, expected in test_cases:
    result = sol.minCostClimbingStairs(cost)
    print("Input:", cost)
    print("Output:", result)
    print("Expected:", expected)
    print("Pass:", result == expected)
    print()