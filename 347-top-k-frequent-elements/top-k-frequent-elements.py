class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countter=Counter(nums)
        ans=[]
        sorted_items = list(sorted(countter.items(), key=lambda x: x[1],reverse=True))
        for i in range(k):
            ans.append(sorted_items[i][0])
        return ans

            