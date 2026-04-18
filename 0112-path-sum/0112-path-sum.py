class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

def build_tree(values):
    if not values:
        return None
    nodes = [None if v is None else TreeNode(v) for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

if __name__ == "__main__":
    s = Solution()
    
    root1 = build_tree([5,4,8,11,None,13,4,7,2,None,None,None,1])
    print(s.hasPathSum(root1, 22))
    
    root2 = build_tree([1,2,3])
    print(s.hasPathSum(root2, 5))
    
    root3 = build_tree([])
    print(s.hasPathSum(root3, 0))