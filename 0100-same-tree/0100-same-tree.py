class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def build_tree(arr):
    if not arr:
        return None
    nodes = [None if x is None else TreeNode(x) for x in arr]
    i = 0
    for j in range(1, len(arr)):
        if nodes[i] is not None:
            if nodes[i].left is None:
                nodes[i].left = nodes[j]
            elif nodes[i].right is None:
                nodes[i].right = nodes[j]
                i += 1
        else:
            i += 1
            j -= 1
    return nodes[0]


s = Solution()

p1 = build_tree([1,2,3])
q1 = build_tree([1,2,3])
print(s.isSameTree(p1, q1))

p2 = build_tree([1,2])
q2 = build_tree([1,None,2])
print(s.isSameTree(p2, q2))

p3 = build_tree([1,2,1])
q3 = build_tree([1,1,2])
print(s.isSameTree(p3, q3))