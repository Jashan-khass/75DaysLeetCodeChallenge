class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root):
        result = []
        stack = []

        if root:
            stack.append(root)

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return result

root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.left.right.left = TreeNode(6)
root2.left.right.right = TreeNode(7)
root2.right.right = TreeNode(8)
root2.right.right.left = TreeNode(9)

root3 = None

root4 = TreeNode(1)

sol = Solution()

print(sol.preorderTraversal(root1))
print(sol.preorderTraversal(root2))
print(sol.preorderTraversal(root3))
print(sol.preorderTraversal(root4))