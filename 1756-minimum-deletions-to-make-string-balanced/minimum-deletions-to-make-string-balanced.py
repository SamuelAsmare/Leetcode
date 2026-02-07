class Solution:
    def minimumDeletions(self, s: str) -> int:
        fre = Counter(s)
        a , b , ans = fre['a'] , 0 , len(s)
        for item in s:
            ans = min(ans , a + b)
            if item == "a":
                a -= 1
            else:
                b += 1
        ans = min(ans , a + b)
        return ans 

