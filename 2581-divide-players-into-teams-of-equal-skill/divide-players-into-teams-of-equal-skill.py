class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left , right = 0 , len(skill)-1
        summ , chemistry = skill[0] + skill[-1]  , 0
        while(left<right):
            if summ != skill[left]+skill[right]:
                return -1
            chemistry += skill[right]*skill[left]
            left += 1
            right -= 1
        return chemistry

