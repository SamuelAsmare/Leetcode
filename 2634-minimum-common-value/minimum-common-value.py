class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s,small=set(nums1),float("inf")
        for i in range (len (nums2)):
            if (nums2[i] in s):
                if(small>nums2[i]):
                    small=nums2[i]
        if (small != float("inf")):
            return small
        return -1   