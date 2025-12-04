class Solution:
    def countCollisions(self, directions: str) -> int:
        ans , stack = 0 , []
        for item in  directions:
            if not stack or item == "R" or item == "S" or stack[-1] == item:
                stack.append(item)
            elif item == "L":
                if stack[-1] == "S":
                    ans += 1
                else:
                    stack[-1] = "S"
                    ans += 2
            collides = True
            while len(stack) >= 2 and collides :
                if stack[-1] == "L":
                    if stack[-2] == "R":
                        ans += 2
                        stack.pop()
                        stack[-1] = "S"
                    elif stack[-2] == "S":
                        stack.pop()
                        ans += 1
                    else:
                        collides = False
                elif stack[-1] == "S":
                    if stack[-2] == "R":
                        ans += 1
                        stack[-2] = "S"
                        stack.pop()
                    else:
                        collides = False
                else:
                    collides = False
        return ans


