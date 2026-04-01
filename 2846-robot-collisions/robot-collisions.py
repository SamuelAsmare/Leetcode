class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        for i , item in enumerate(positions):
            positions[i] = [item , healths[i] , directions[i],i]
        positions.sort()
        stack = []
        for item in positions:
            flag = True
            while stack and not(stack[-1][2] != "R" or item[2] != "L"):
                if stack[-1][1] > item[1]:
                    stack[-1][1] -= 1
                    flag = False
                    break
                elif stack[-1][1] == item[1]:
                    stack.pop()
                    flag = False
                    break
                else:
                    stack.pop()
                    item[1] -= 1
            if flag:
                stack.append(item)
        stack.sort(key = lambda x:x[3])
        return [item[1] for item in stack]
        







