class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans , fre , summ =  [] , Counter(s) , 0
        left , right = 0 , len(s)-1
        for i in range(len(s)):
            fre[s[i]]-=1
            if fre[s[i]]==0:
                del fre[s[i]]
            exists = False
            for j in range(0,i+1):
                if s[j] in fre:
                    exists = True
                    break
            if not exists:
                    ans.append(i+1-summ)
                    summ+=(i+1-summ)
        return ans
                

