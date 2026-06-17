class Solution:
    def minimumLines(self, stockPrices):
        n = len(stockPrices)
        if n <= 1:
            return 0

        stockPrices.sort()
        lines = 1

        for i in range(2, n):
            x1, y1 = stockPrices[i - 2]
            x2, y2 = stockPrices[i - 1]
            x3, y3 = stockPrices[i]

            if (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1):
                lines += 1

        return lines


sol = Solution()

cases = [
    ([[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]], 3),
    ([[3,4],[1,2],[7,8],[2,3]], 1)
]

for arr, expected in cases:
    result = sol.minimumLines(arr)
    print("Input:", arr)
    print("Output:", result)
    print("Expected:", expected)
    print()