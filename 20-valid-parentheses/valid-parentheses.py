class Solution:
    def isValid(self, s: str) -> bool:
        dic={ "]":"[","}":"{", ")":"("}
        stack=[]
        for i, item in enumerate(s):
            if(item not in dic):
                stack.append(item)
            else:
                if(stack):
                    if(dic[item]!=stack[-1]):
                        return False
                    stack.pop()
                else:
                    return False
        if(stack):
            return False
        return True