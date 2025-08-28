class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans  , fre = [] , Counter(nums)
        while(fre):
            row = []  
            for item in list(fre.keys()):
                row.append(item)
                fre[item] -= 1
                if fre[item] == 0:
                    del fre[item]
            ans.append(row)
        return ans
            
        