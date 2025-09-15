class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_numbers = [item for item in nums if item>0]
        negative_numbers= [item for item in nums if item<0]
        ans = []
        for i , item in enumerate(positive_numbers):
            ans.append(item)
            ans.append(negative_numbers[i])
        return ans