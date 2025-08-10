class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        setA = set()
        setB , ans = set() , []
        for i, item in enumerate(A):
            setA.add(item)
            setB.add(B[i])
            ans.append(len(setA & setB))
        return ans

         