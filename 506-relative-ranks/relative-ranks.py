class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp=score.copy()
        def heapify(arr,n,i):
            larger=i
            left = 2 * i + 1
            right= 2 * i + 2
            if (left<n and arr[left] > arr[larger]):
                larger=left
            if (right<n and arr[right]>arr[larger]):
                larger=right
            if larger !=i:
                arr[i],arr[larger] = arr[larger],arr[i]
                heapify(arr,n,larger)
        def call(arr):
            n=len(arr)
            for i in range(n//2-1,-1,-1):
                heapify(arr,n,i)
        call(temp)
        def findlarg(arr):
            dic,counter,n={},1,len(arr)-1
            dic[arr[0]]=1
            while (n>0):
                arr[0]=arr[-1]
                arr.pop()
                heapify(arr,n,0)  # i am calling the function
                counter+=1
                dic[arr[0]]=counter
                n-=1
            return dic
        dic=findlarg(temp)
        for i in range(len(score)):
            if(dic[score[i]]==1):
                score[i]="Gold Medal"
            elif(dic[score[i]]==2):
                score[i]="Silver Medal"
            elif(dic[score[i]]==3):
                score[i]="Bronze Medal"
            else:
                score[i]=str(dic[score[i]])
        print(dic)
        return score
            

            

