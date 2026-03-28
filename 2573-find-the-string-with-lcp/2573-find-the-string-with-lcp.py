class Solution(object):
    def findTheString(self, lcp):
        n = len(lcp)
        
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""
            for j in range(n):
                if lcp[i][j] != lcp[j][i]:
                    return ""
        
        res = [''] * n
        cur = 0
        
        for i in range(n):
            if res[i] == '':
                if cur >= 26:
                    return ""
                ch = chr(ord('a') + cur)
                for j in range(i, n):
                    if lcp[i][j] > 0:
                        res[j] = ch
                cur += 1
        
        word = "".join(res)
        
        dp = [[0]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word[i] == word[j]:
                    if i == n-1 or j == n-1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = 0
        
        for i in range(n):
            for j in range(n):
                if dp[i][j] != lcp[i][j]:
                    return ""
        
        return word


if __name__ == "__main__":
    sol = Solution()
    
    tests = [
        ([[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]], "abab"),
        ([[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]], "aaaa"),
        ([[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]], "")
    ]
    
    for i in range(len(tests)):
        lcp, expected = tests[i]
        result = sol.findTheString(lcp)
        if result == expected:
            print("Test", i+1, ": PASS | Output:", result)
        else:
            print("Test", i+1, ": FAIL | Output:", result, "| Expected:", expected)