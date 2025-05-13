class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        stack = [s[0]]
        if(stack[-1] == "#"):
            stack.pop()


        for item in s[1:]:
            if item == "#" and stack: 
                stack.pop()
            elif(item == "#" and not stack):
                continue
            else:
                stack.append(item)
        
        s = "".join(stack)



        stack = [t[0]]
        if(stack[-1] == "#"):
            stack.pop()

            
        for item in t[1:]:
            if item == "#" and stack:
                stack.pop()
            elif(item == "#" and not stack):
                continue
            else:
                stack.append(item)
        
        t = "".join(stack)
        print (s,t)
        return t == s


