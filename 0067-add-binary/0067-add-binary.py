class Solution:
    def addBinary(self, a, b):
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = ""

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            result = str(total % 2) + result
            carry = total // 2

        return result


s = Solution()

test_cases = [
    ("11", "1"),
    ("1010", "1011")
]

for a, b in test_cases:
    print("a =", a, "b =", b, "->", s.addBinary(a, b))