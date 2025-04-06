class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans=[]
        for i in range(len(boxes)):
            Sum=0
            for j in range(len(boxes)):
                if(i==j):
                    continue
                else:
                    if(boxes[j]=='1'):
                        Sum+=abs(i-j)
            ans.append(Sum)
        return ans

            