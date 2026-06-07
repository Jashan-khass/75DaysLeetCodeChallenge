class Solution:
    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([1, 2, 5], 11),
        ([2], 3),
        ([1], 0)
    ]

    for coins, amount in test_cases:
        print("Coins:", coins)
        print("Amount:", amount)
        print("Minimum Coins:", sol.coinChange(coins, amount))
        print("-" * 30)