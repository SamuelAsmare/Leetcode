class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        group , ans  = defaultdict(int) , 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                group[nums[i]*nums[j]]+=1
        print(group)
        for item in group.values():
            if item>2:
                ans += (item**2) - (item*2)
        return ans 