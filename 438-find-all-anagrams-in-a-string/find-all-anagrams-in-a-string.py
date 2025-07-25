class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        countp=Counter(p)
        k=len(p)
        ans=[]
        counts=Counter(s[:k])
        for left in range(len(s)-k+1):
            if(counts==countp):
                ans.append(left)
            counts[s[left]]-=1
            if(counts[s[left]]==0): # if the counter becomes 0 delete the character
               del counts[s[left]]
            if(left+k  <len(s)):
                counts[s[left+k]]+=1
            
        return ans
