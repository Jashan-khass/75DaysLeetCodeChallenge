class Solution:
    def characterReplacement(self, s, k):
        count = {}
        left = 0
        maxf = 0
        res = 0
        
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxf = max(maxf, count[s[right]])
            
            while (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res


def run_tests():
    sol = Solution()
    
    test_cases = [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4)
    ]
    
    for i in range(len(test_cases)):
        s, k, expected = test_cases[i]
        result = sol.characterReplacement(s, k)
        print("Test Case", i + 1)
        print("Input:", s, k)
        print("Output:", result)
        print("Expected:", expected)
        if result == expected:
            print("Pass")
        else:
            print("Fail")
        print("-" * 30)


if __name__ == "__main__":
    run_tests()