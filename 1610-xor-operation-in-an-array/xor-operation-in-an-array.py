class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr=[]
        for i in range (n):
            arr.append(start+2*i)
        for i in range (n-1):
            if(arr[i]!=arr[i+1]):
                arr[i+1]=arr[i]^arr[i+1]
            else:
                arr[i+1]=0
        return arr[n-1]
