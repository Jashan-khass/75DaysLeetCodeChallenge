class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root):
        def helper(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)
        return helper(root, float('-inf'), float('inf'))

s = Solution()

root1 = TreeNode(2, TreeNode(1), TreeNode(3))
print(s.isValidBST(root1))

root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4, TreeNode(3), TreeNode(6))
print(s.isValidBST(root2))