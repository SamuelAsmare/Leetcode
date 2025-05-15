class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans , n = set() , len(s)
        for i in range(1<<n):
            temp = list(s)
            for j in range(n):
                if temp[j].isalpha():
                    if i & (1<<j):
                        temp[j] = temp[j].swapcase()
            ans.add("".join(temp))

        return  list(ans)

