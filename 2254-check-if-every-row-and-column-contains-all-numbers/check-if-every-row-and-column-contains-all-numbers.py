class Solution(object):
    def checkValid(self, matrix):
        for i in range(len(matrix)):
            if(len(set(matrix[i]))!=len(matrix[i])):
                return False
        transpose=[[row[i] for row in matrix] for i in range(len(matrix[0]))]
        for i in range(len(transpose)):
            if(len(set(transpose[i]))!=len(transpose[i])):
                return False
        return True
            
        