class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # transposwe
        for _ in range(4):
            for i in range(len(mat)):
                for j in range(i , len(mat)):
                    mat[i][j] , mat[j][i] = mat[j][i] , mat[i][j]
            mat.reverse()
            if mat == target:
                return True
        return False