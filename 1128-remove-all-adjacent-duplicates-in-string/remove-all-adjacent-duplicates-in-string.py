class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = [s[0]]
        if not stack:
            return stck
        for j in s[1:]:
            if not stack:
                stack.append(j)
            elif stack[-1] == j:
                stack.pop()
            else:
                stack.append(j)
        return ("".join(stack))