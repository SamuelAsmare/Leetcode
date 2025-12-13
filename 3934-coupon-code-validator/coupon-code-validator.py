class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        n , business  = len(code), {"electronics", "grocery", "pharmacy", "restaurant"}
        ans = []
        for i in range(n):
            if isActive[i] and businessLine[i] in business and code[i]:
                for char in code[i]:
                    if not char.isalnum() and char != "_":
                        break
                else:
                    ans.append([ code[i] , businessLine[i] ])
        ans.sort( key = lambda x : ( x[1] , x[0] ))
        return [ item[0] for item in ans ]


