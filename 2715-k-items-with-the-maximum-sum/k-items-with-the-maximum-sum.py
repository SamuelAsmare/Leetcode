class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k<=numOnes:
            return k
        elif k <= numOnes + numZeros:
            return numOnes
        else:
            summ = numOnes + numZeros
            if (summ) < k:
                return numOnes - (k-(numZeros+numOnes))
            return numOnes - numNegOnes