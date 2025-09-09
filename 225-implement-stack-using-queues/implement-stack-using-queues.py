from collections import deque
class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        pop = self.stack.pop()
        return pop
    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        ans = len(self.stack) == 0
        return ans


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()