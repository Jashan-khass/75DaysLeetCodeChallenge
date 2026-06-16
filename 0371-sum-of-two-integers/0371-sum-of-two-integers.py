class Solution:
    def getSum(self, a, b):
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        return a if a <= max_int else ~(a ^ mask)

sol = Solution()

cases = [
    (1, 2),
    (2, 3)
]

for a, b in cases:
    print(a, b, "->", sol.getSum(a, b))