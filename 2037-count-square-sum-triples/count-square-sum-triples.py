class Solution:
    def countTriples(self, n: int) -> int:
        se=set()
        for i in range(1,n+1):
            se.add(i*i)
        li=list(se)
        li.sort()
        n=len(li)
        count=0
        for i in range(n-1,0,-1):
            temp=i-1
            while (temp>=0):
                if(li[i]-li[temp] in se):
                    count+=1
                temp-=1
        return count