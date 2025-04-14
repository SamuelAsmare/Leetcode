class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest=0
        for i ,item in enumerate(accounts):
            richest=max(sum(accounts[i]),richest)
        return richest