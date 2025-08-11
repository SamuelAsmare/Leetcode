class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        fre , n , ans = Counter(arr) , len(arr)//2 , 0 
        sorted_fre = sorted(fre.items(), key=lambda x:-x[1])
        print(sorted_fre)
        for i , item in enumerate(sorted_fre):
            ans += item[1]
            if ans>=n:
                return i+1
        return n
