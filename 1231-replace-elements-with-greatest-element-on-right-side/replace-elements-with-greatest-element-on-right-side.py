class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr)==1:
            return [-1]
        maxval = -1
        for i in range(len(arr)-1 , -1 , -1):
            temp = arr[i]
            arr[i] = maxval
            maxval = max(maxval,temp)
        return arr



        