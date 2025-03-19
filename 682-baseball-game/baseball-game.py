class Solution(object):
    def calPoints(self, operations):
        ans=[]
        for i in range(len(operations)):
            if(operations[i]=="+"):
                ans.append(int(ans[-1]) + int(ans[-2]))
            elif(operations[i]=="D"):
                ans.append(int(ans[-1])*2)
            elif(operations[i]=="C"):
                ans.pop()
            else:
                ans.append(int(operations[i]))

        return sum(ans)


        