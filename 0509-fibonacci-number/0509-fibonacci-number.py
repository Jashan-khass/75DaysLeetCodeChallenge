class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1

        a, b = 1, 1

        for i in range(3, n + 1):
            a, b = b, a + b

        return b