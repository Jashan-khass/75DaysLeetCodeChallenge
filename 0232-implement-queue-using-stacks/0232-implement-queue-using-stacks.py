class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def move(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

    def pop(self):
        self.move()
        return self.s2.pop()

    def peek(self):
        self.move()
        return self.s2[-1]

    def empty(self):
        return not self.s1 and not self.s2


# -------- Driver Code (LeetCode Style Test Cases) --------

def run_test(operations, values):
    obj = None
    result = []

    for op, val in zip(operations, values):
        if op == "MyQueue":
            obj = MyQueue()
            result.append(None)
        elif op == "push":
            obj.push(val[0])
            result.append(None)
        elif op == "pop":
            result.append(obj.pop())
        elif op == "peek":
            result.append(obj.peek())
        elif op == "empty":
            result.append(obj.empty())

    print(result)


# -------- Test Cases --------

# Case 
run_test(
    ["MyQueue","push","push","peek","pop","empty"],
    [[],[1],[2],[],[],[]]
)
