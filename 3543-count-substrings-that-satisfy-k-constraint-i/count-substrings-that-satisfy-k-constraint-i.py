class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        # substr=[s[i:j+1] for i in range(len(s)) for j in range(i,len(s))]
        # count=0
        # for i in range(len (substr)):
        #     if(substr[i].count('0')<=k or substr[i].count('1')<=k):
        #         count+=1
        # return count
        left =0
        zero = 0
        one = 0
        ans = 0
        for right in range(len(s)):
            if s[right] == '0':
                zero+=1
            else:
                one+=1
            
            while zero>k and one>k:
                if s[left] == '0':
                    zero-=1
                else:
                    one-=1
                left+=1
            ans+=right-left+1
        return ans

