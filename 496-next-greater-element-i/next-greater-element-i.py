class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #  i will have stack , ans
        stack  , ans  = [] , dict()
        for i,item in enumerate(nums2):
            while stack and nums2[stack[-1]] < item:
                ans[nums2[stack[-1]]] = item
                stack.pop()
            stack.append(i)
            ans[item] = -1
        return [ans[val] for val in nums1]            

