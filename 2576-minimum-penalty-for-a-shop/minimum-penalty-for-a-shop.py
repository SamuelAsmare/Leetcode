class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ys = customers.count("Y") 
        ns = 0                      
        min_penalty = ys           
        ans = 0
        for i, state in enumerate(customers):
            if state == 'Y':
                ys -= 1
            else:
                ns += 1
            if ns + ys < min_penalty:
                min_penalty = ns + ys
                ans = i + 1  
        return ans
