class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        dic,temp,n={},score.copy(),len(score)
        temp.sort()
        for i in range(n):
            dic[temp[i]]=n-i
        for i in range(n):
            if (dic[score[i]]==1):
                score[i]="Gold Medal"
            elif(dic[score[i]]==2):
                score[i]="Silver Medal"
            elif(dic[score[i]]==3):
                score[i]="Bronze Medal"
            else:
                score[i]=str(dic[score[i]])
        return score
            

            

