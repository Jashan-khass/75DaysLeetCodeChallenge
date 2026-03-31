class Solution:
    def generateString(self, str1, str2):
        n = len(str1)
        m = len(str2)
        res = ['?'] * (n + m - 1)

        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if res[i + j] == '?' or res[i + j] == str2[j]:
                        res[i + j] = str2[j]
                    else:
                        return ""

        for i in range(n + m - 1):
            if res[i] == '?':
                res[i] = 'a'

        for i in range(n):
            if str1[i] == 'F':
                if ''.join(res[i:i+m]) == str2:
                    changed = False

                    for j in range(m-1, -1, -1):
                        idx = i + j
                        old = res[idx]

                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            if c == str2[j]:
                                continue

                            res[idx] = c

                            valid = True
                            for k in range(max(0, idx - m + 1), min(n, idx + 1)):
                                sub = ''.join(res[k:k+m])
                                if str1[k] == 'T' and sub != str2:
                                    valid = False
                                    break

                            if valid:
                                changed = True
                                break

                            res[idx] = old

                        if changed:
                            break

                    if not changed:
                        return ""

        for i in range(n):
            sub = ''.join(res[i:i+m])
            if (str1[i] == 'T' and sub != str2) or (str1[i] == 'F' and sub == str2):
                return ""

        return ''.join(res)


s = Solution()

print(s.generateString("TFTF", "ab"))
print(s.generateString("TFTF", "abc"))
print(s.generateString("F", "d"))
print(s.generateString("FT", "wvxyy"))