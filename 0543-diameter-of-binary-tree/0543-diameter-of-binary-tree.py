class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        self.d = 0
        
        def f(node):
            if not node:
                return 0
            l = f(node.left)
            r = f(node.right)
            self.d = max(self.d, l + r)
            return 1 + max(l, r)
        
        f(root)
        return self.d

s = Solution()

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
print(s.diameterOfBinaryTree(root1))

root2 = TreeNode(1)
root2.left = TreeNode(2)
print(s.diameterOfBinaryTree(root2))