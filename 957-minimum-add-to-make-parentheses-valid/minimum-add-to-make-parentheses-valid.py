class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        need = added = 0   
        for item in s:
            if item == '(': # if it is open i need closing
                need += 1  
            elif item == ')': # if it is closing, will decrease the opens other wise add to answer
                if need > 0:
                    need -= 1  
                else:
                    added += 1
        return added + need