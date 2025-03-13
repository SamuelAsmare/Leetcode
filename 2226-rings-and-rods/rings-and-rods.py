class Solution:
    def countPoints(self, rings: str) -> int:
        counter=0
        ring=list(rings)
        for i in range(10):
            G=False
            B=False
            R=False
            for j in range(1,len(ring),+2):
                if(chr(48+i) not in ring):
                    break
                else:
                    if(ring[j]==chr(48+i)):
                        if(ring[j-1]=='B'):
                            B=True
                        elif(ring[j-1]=='G'):
                            G=True
                        elif(ring[j-1]=='R'):
                            R=True
            if(B and G and R):
                counter+=1
        return counter