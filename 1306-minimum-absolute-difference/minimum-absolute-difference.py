class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        # find minimum difference
        diff , ans = float("inf") , []
        for i in range(len(arr)-1):
            diff = min(diff , arr[i+1] - arr[i])
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == diff:
                ans.append([arr[i] , arr[i+1]])
        return ans


    
            
            
