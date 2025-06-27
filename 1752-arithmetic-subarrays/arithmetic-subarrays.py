class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            subarray = nums[l[i] : r[i]+1]
            subarray.sort()
            difference = subarray[1]-subarray[0]
            is_arithimetic = True
            for j in range(len(subarray)-1):
                if subarray[j+1]-subarray[j]!=difference:
                    is_arithimetic=False
                    break
            ans.append(is_arithimetic)
        return ans


