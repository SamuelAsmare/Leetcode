class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sam=Counter(nums)
        sor=sorted(sam.items(), key=lambda x:x[1], reverse=True)
        return (sor[0][0])