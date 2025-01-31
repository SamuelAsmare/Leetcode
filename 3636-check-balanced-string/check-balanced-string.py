class Solution(object):
    def isBalanced(self, num):
        sumeven=0
        sumodd=0
        for i in range(len(num)):
            if(i%2!=0):
                sumodd=sumodd+int(num[i])
            else:
                sumeven=sumeven+int(num[i])
        return sumeven==sumodd
        
        