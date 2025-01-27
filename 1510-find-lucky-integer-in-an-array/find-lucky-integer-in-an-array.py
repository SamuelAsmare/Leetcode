class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort()
        arr.reverse()
        fre=Counter(arr)
        for i in range(0,len(arr)):
            if(fre[arr[i]]==arr[i]):
                return arr[i]
        return -1