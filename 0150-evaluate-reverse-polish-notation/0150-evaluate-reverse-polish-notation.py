class Solution:
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:
                    if a * b < 0:
                        stack.append(- (abs(a) // abs(b)))
                    else:
                        stack.append(a // b)
        return stack[0]


if __name__ == "__main__":
    sol = Solution()
    
    print(sol.evalRPN(["2","1","+","3","*"]))  
    print(sol.evalRPN(["4","13","5","/","+"]))  
    print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))  