class Solution:
    def simplifyPath(self, path: str) -> str:
        folders = path.split("/")
        stack =  [] 
        for item in folders:
            if item == "" or item == ".":
                continue
            if item == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(item)
        return "/" + "/".join(stack)
            
       