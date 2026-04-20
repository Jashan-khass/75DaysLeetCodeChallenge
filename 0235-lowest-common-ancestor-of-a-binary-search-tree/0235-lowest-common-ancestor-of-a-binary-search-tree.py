class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root

def build_tree():
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    return root

root = build_tree()
sol = Solution()

p = root.left
q = root.right
print(sol.lowestCommonAncestor(root, p, q).val)

p = root.left
q = root.left.right
print(sol.lowestCommonAncestor(root, p, q).val)

root2 = TreeNode(2)
root2.left = TreeNode(1)
p = root2
q = root2.left
print(sol.lowestCommonAncestor(root2, p, q).val)