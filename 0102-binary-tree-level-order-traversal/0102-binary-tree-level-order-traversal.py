from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        q = deque([root])
        result = []

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(level)

        return result

def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    q = deque([root])
    i = 1

    while q and i < len(values):
        node = q.popleft()

        if values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1

    return root

if __name__ == "__main__":
    sol = Solution()

    # Case 1
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    print(sol.levelOrder(root1)) 

    # Case 2
    root2 = build_tree([1])
    print(sol.levelOrder(root2)) 

    # Case 3
    root3 = build_tree([])
    print(sol.levelOrder(root3))  