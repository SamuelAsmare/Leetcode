class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        fre,n=Counter(blocks[:k]),len(blocks)
        small=fre['W']
        for i in range(k,n):
            fre[blocks[i]]+=1
            fre[blocks[i-k]]-=1
            small=min(small,fre["W"])
        return small
        
