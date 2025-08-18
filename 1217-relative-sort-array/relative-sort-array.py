class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        fre = Counter(arr1)
        ans = []
        non_available = []
        for item in arr1:
            if item not in arr2:
                non_available.append(item)
        for item in arr2:
            ans.extend([item]*fre[item])
        non_available.sort()
        ans.extend(non_available)
        return ans
        
