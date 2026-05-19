from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right

def build_tree(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

def find_node(root, value):
    if not root:
        return None

    if root.val == value:
        return root

    left = find_node(root.left, value)
    if left:
        return left

    return find_node(root.right, value)

root1 = build_tree([3,5,1,6,2,0,8,None,None,7,4])
p1 = find_node(root1, 5)
q1 = find_node(root1, 1)

root2 = build_tree([3,5,1,6,2,0,8,None,None,7,4])
p2 = find_node(root2, 5)
q2 = find_node(root2, 4)

root3 = build_tree([1,2])
p3 = find_node(root3, 1)
q3 = find_node(root3, 2)

solution = Solution()

print(solution.lowestCommonAncestor(root1, p1, q1).val)
print(solution.lowestCommonAncestor(root2, p2, q2).val)
print(solution.lowestCommonAncestor(root3, p3, q3).val)