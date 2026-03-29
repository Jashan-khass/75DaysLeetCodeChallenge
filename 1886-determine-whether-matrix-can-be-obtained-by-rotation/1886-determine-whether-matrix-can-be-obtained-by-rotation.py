class Solution:
    def findRotation(self, mat, target):
        def rotate(matrix):
            return [list(row) for row in zip(*matrix[::-1])]

        for _ in range(4):
            if mat == target:
                return True
            mat = rotate(mat)
        return False
s = Solution()
print(s.findRotation([[0,1],[1,0]], [[1,0],[0,1]]))
print(s.findRotation([[0,1],[1,1]], [[1,0],[0,1]]))
print(s.findRotation([[0,0,0],[0,1,0],[1,1,1]], [[1,1,1],[0,1,0],[0,0,0]]))