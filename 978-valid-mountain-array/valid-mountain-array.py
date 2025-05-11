class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if(len(arr)==1) or arr[0] > arr[1] or arr[-1] > arr[-2] :
            return False
        seen = False
        for i in range(1,len(arr)):
            if(arr[i] == arr[i-1]):
                return False
            if arr[i-1] > arr[i]:
                seen = True
            if seen and arr[i]>=arr[i-1]:
                return False
        return True