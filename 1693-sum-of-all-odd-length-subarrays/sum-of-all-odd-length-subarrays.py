class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        Sum,n=0,len(arr)
        for i in range(n):
            for j in range(i,n):
                if (j-i+1)%2!=0:
                    Sum+=sum(arr[i:j+1])
        return Sum
