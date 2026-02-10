class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            even_fre = defaultdict(int)
            odd_fre = defaultdict(int)
            for j in range(i,len(nums)):
                if nums[j] & 1:
                    odd_fre[nums[j]] += 1
                else:
                    even_fre[nums[j]] += 1
                if len(even_fre) == len(odd_fre):
                    ans = max(ans , j - i + 1 )
        return ans

