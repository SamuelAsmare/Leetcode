class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # index = relative position
        # |value|  =  size
        # sign = direction [-2 , -2 , ]
        stack = []
        for item in asteroids:
            while stack and stack[-1] > 0 and item < 0:
                if abs(stack[-1]) < abs(item):
                    stack.pop()
                    continue  
                elif abs(stack[-1]) == abs(item):
                    stack.pop()
                break
            else:
                stack.append(item)
        return stack
