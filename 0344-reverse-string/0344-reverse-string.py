class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

if __name__ == "__main__":
    sol = Solution()
    
    cases = [
        ["h","e","l","l","o"],
        ["H","a","n","n","a","h"]
    ]
    
    for i, case in enumerate(cases):
        original = case[:]
        sol.reverseString(case)
        print("Case {}: {} -> {}".format(i+1, original, case))