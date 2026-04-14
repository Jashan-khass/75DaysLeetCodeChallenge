class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

def build_tree(arr):
    if not arr:
        return None
    nodes = [None if x is None else TreeNode(x) for x in arr]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

def tree_to_list(root):
    if not root:
        return []
    res, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)
    while res and res[-1] is None:
        res.pop()
    return res

cases = [
    [4,2,7,1,3,6,9],
    [2,1,3],
    []
]

sol = Solution()
for case in cases:
    root = build_tree(case)
    inverted = sol.invertTree(root)
    print(tree_to_list(inverted))