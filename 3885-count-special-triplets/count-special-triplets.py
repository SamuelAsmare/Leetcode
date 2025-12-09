class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        #  we directly need before n// 2 and after n*2
        MOD = 10**9 + 7
        n = len(nums)
        multiplied_by_2 = [0]*n
        fre = Counter(nums)
        before = defaultdict(int)
        ans = 0
        for item in nums:
            fre[item] -= 1
            if fre[item] == 0:
                del fre[item]
            if item * 2 in fre:
                ans = (ans + (before[item*2]*fre[item*2]))%MOD
            before[item] += 1
        return ans

                


       




        
