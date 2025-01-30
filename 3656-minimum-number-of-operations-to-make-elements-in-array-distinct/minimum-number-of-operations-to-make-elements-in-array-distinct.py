class Solution(object):
    def minimumOperations(self, nums):
        reversed=nums[::-1]
        print(reversed)
        arr=[]
        for i in range(len(reversed)):
            if(reversed[i] in arr):
                break    
            arr.append(reversed[i]) 
        newsize=len(reversed)-len(arr)
        if newsize%3==0:
            return newsize//3
        else:
          return newsize//3+1
       
        