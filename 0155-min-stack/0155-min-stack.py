class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


ops = ["MinStack","push","push","push","getMin","pop","top","getMin"]
vals = [[],[-2],[0],[-3],[],[],[],[]]

outputs = []
minStack = None

for op, val in zip(ops, vals):
    if op == "MinStack":
        minStack = MinStack()
        outputs.append(None)
    elif op == "push":
        minStack.push(val[0])
        outputs.append(None)
    elif op == "pop":
        minStack.pop()
        outputs.append(None)
    elif op == "top":
        outputs.append(minStack.top())
    elif op == "getMin":
        outputs.append(minStack.getMin())

print(outputs)