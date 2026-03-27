class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        temp = deepcopy(mat)
        for _ in range(k):
            for i in range(len(mat)):
                if not i & 1:
                    for j in range(len(mat[0]) - 1):
                        mat[i][j] , mat[i][j+1] = mat[i][j+1] , mat[i][j]
                else:
                    for j in range(1,len(mat[0])):
                        mat[i][j] , mat[i][j - 1] = mat[i][j-1] , mat[i][j]
        return mat == temp

