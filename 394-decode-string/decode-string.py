class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                part = ""
                while stack[-1] != "[":
                    part = stack.pop() + part
                stack.pop() # remove the opening bracket
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k)*part)
        return  "".join(stack)
 
                