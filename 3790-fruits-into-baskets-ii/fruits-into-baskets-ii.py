class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count=0
        for i in range(len(fruits)):
            exists=False
            for j in range(len(baskets)):
                if fruits[i] <= baskets[j]:
                    exists=True
                    baskets.remove(baskets[j])
                    break
            if(not exists):
                count+=1
        return count