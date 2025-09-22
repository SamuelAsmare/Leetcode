class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n=len(blocks) # checking the length of the list
        fre=Counter(blocks[:k]) # i am getting the initial frequenct
        small=fre['W']
        for i in range(k,n):
            fre[blocks[i]]+=1
            fre[blocks[i-k]]-=1
            small=min(small,fre["W"])
        return small
