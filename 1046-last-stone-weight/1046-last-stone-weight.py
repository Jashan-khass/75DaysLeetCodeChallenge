import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)

            if y != x:
                heapq.heappush(stones, -(y - x))

        return -stones[0] if stones else 0


solver = Solution()

test_cases = [
    ([2, 7, 4, 1, 8, 1], 1),
    ([1], 1),
    ([3, 3], 0),
    ([10, 4, 2, 10], 2),
    ([9, 3, 2, 10], 0)
]

for stones, expected in test_cases:
    result = solver.lastStoneWeight(stones)
    print("Input:", stones)
    print("Output:", result)
    print("Expected:", expected)
    print("Pass:", result == expected)
    print("--------------------")