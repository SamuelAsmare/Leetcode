class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans , size , temp = [ ] , len(original) , []
        if n*m != size: return []
        for i in range(0,size,+n):
            temp = original[i:i+n]
            ans.append(temp)
        return ans
