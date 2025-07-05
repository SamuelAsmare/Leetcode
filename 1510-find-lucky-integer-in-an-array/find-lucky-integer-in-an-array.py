class Solution:
    def findLucky(self, arr: List[int]) -> int:
        fre ,ans  = Counter(arr) , -1
        for item in fre:
            if fre[item]==item:ans=max(ans,item)
        return ans