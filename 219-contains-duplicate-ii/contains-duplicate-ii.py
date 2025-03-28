class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s=set(nums[:k])
        if(len(s)!= len(nums[:k])):
            return True
        for i in range(k,len(nums)):
            if(nums[i] in s):
                return True
            s.add(nums[i])
            s.remove(nums[i-k])
        return False
