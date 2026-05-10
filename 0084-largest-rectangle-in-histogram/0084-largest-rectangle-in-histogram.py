class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)

        return max_area


s = Solution()

test_cases = [
    ([2, 1, 5, 6, 2, 3], 10),
    ([2, 4], 4)
]

for i, (heights, expected) in enumerate(test_cases):
    result = s.largestRectangleArea(heights[:])
    print("Test Case", i + 1)
    print("Input:", heights)
    print("Expected:", expected)
    print("Output:", result)
    print("Pass:", result == expected)
    print("--------------------")