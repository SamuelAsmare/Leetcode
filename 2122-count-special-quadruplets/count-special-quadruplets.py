class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        se=set(nums)
        n=len(nums)
        dic = Counter(nums)
        count=0
        for d in range(n-1,2,-1):
            c=d-1
            while(c>=2):
                b=c-1
                while(b>=1):
                    if(nums[d]-nums[b]-nums[c] in nums[:b]):
                        count+=(nums[:b].count(nums[d]-nums[b]-nums[c]))
                        print(b, c, d)
                    b-=1
                c-=1
        return count

