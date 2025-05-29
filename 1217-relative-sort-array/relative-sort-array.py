class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort()
        res = []
        for i in range(len(arr2)):
            while(arr2[i] in arr1):
                res.append(arr2[i])
                arr1.remove(arr2[i])
        res += arr1
        return res
