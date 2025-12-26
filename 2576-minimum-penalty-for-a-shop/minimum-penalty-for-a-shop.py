class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ys , ans , ns ,n = customers.count("Y") , 0 , 0 , len(customers)
        pen = n
        for i , state in enumerate(customers):
            if pen > ys + ns:
                ans = i
                pen = ys + ns
            if state == "Y":
                ys -= 1
            else:
                ns += 1
        if pen > ys + ns :
           return n    
        return ans 


# [YYNY] = ANS = 0
# 





