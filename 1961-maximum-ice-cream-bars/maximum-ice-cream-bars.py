class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        counter=0
        for i in costs:
            if coins>=i:
                coins-=i
                counter+=1
        return counter

