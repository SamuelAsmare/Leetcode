class Solution(object):
    def checkIfExist(self, arr):
        for i in range(len(arr)):
            if(arr[i]==0):
                arr[i]=1
                if(0 in arr):
                    return True
            if(2*arr[i] in arr):
                return True
        return False
        