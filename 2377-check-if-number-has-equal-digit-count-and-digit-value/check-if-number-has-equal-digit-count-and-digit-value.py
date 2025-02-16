class Solution:
    def digitCount(self, num: str) -> bool:
        digitarr=[int(digits) for digits in str(num)]
        fre=Counter(digitarr)
        check=True
        for i in range(len(digitarr)):
            if(fre[i]!=digitarr[i]):
                check=False
                break
        return check
        