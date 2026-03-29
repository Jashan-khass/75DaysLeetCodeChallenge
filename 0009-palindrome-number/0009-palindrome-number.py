class Solution:
    def isPalindrome(self, x):
        s = str(x)
        return s == s[::-1]
obj = Solution()

print(obj.isPalindrome(121))    # True
print(obj.isPalindrome(-121))   # False
print(obj.isPalindrome(10))     # False