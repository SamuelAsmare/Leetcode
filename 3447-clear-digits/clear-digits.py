class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            curr=s[i]
            if (not curr.isdigit()):
                stack.append(curr)
            else:
                stack.pop()
        return "".join(stack)