class Solution:
    def areSimilar(self, mat, k):
        m, n = len(mat), len(mat[0])
        k %= n

        for i in range(m):
            if i % 2 == 0:
                if mat[i] != mat[i][k:] + mat[i][:k]:
                    return False
            else:
                if mat[i] != mat[i][-k:] + mat[i][:-k]:
                    return False

        return True


# test cases
s = Solution()
print(s.areSimilar([[1,2,3],[4,5,6],[7,8,9]], 4))
print(s.areSimilar([[1,2,1,2],[5,5,5,5],[6,3,6,3]], 2))
print(s.areSimilar([[2,2],[2,2]], 3))