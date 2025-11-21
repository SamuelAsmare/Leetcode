class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dic = dict()
        ans = 1
        for i in range(len(arr)-1 , -1 , -1):
            if arr[i] + difference in dic:
                current = dic[arr[i] + difference] + 1
                dic[arr[i]] = current
                ans = max(ans , current)
            else:
                dic[arr[i]] = 1
        return ans