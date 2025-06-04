class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        fre , i = Counter(arr) , 0
        for item in fre:
            if fre[item] == 1:
                i+=1
            if i == k:
                return item
        return ""