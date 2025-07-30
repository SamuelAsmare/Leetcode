class Solution:
    def isValid(self, s: str) -> bool:
        dictionary={ "]":"[","}":"{", ")":"("}
        stack=[]
        for i, item in enumerate(s):
            if(item not in dictionary):
                stack.append(item)
            else:
                if(stack):
                    if(dictionary[item]!=stack[-1]):
                        return False
                    stack.pop()
                else:
                    return False
        if(stack):
            return False
        return True