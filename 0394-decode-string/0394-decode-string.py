class Solution:
    def decodeString(self, s):
        stack = []
        curr_num = 0
        curr_str = ""

        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)

            elif ch == '[':
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0

            elif ch == ']':
                prev_str, num = stack.pop()
                curr_str = prev_str + curr_str * num

            else:
                curr_str += ch

        return curr_str


sol = Solution()

print(sol.decodeString("3[a]2[bc]"))
print(sol.decodeString("3[a2[c]]"))
print(sol.decodeString("2[abc]3[cd]ef"))