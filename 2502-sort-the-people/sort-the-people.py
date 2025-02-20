class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        arr=[]
        ans=[]
        for i in range(len(names)):
           arr.append([names[i], heights[i]])
        arr.sort(key=lambda x:x[1])
        arr.reverse()
        for i in range(len(names)):
            ans.append(arr[i][0])
        return ans

        