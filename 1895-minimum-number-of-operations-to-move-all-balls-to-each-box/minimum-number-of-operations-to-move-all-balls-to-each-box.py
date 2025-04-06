class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans,n=[],len(boxes)
        for i in range(n):
            Sum=0
            for j in range(n):
                if(i==j):
                    continue
                else:
                    if(boxes[j]=='1'):
                        Sum+=abs(i-j)
            ans.append(Sum)
        return ans

            