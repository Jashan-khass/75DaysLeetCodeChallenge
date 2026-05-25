from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):
        freq = list(Counter(tasks).values())
        max_freq = max(freq)
        max_count = freq.count(max_freq)

        return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)


if __name__ == "__main__":
    s = Solution()

    tasks1 = ["A","A","A","B","B","B"]
    n1 = 2
    print(s.leastInterval(tasks1, n1))

    tasks2 = ["A","C","A","B","D","B"]
    n2 = 1
    print(s.leastInterval(tasks2, n2))

    tasks3 = ["A","A","A","B","B","B"]
    n3 = 3
    print(s.leastInterval(tasks3, n3))