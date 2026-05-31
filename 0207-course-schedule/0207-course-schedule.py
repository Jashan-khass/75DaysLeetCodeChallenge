from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        completed = 0

        while q:
            node = q.popleft()
            completed += 1

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return completed == numCourses


sol = Solution()

test_cases = [
    (2, [[1, 0]], True),
    (2, [[1, 0], [0, 1]], False)
]

for i in range(len(test_cases)):
    numCourses, prerequisites, expected = test_cases[i]
    result = sol.canFinish(numCourses, prerequisites)

    print("Test Case", i + 1)
    print("Input:", numCourses, prerequisites)
    print("Output:", result)
    print("Expected:", expected)
    print("Pass:", result == expected)
    print()