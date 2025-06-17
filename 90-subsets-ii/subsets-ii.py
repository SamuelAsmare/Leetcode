class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ans , n = set() , len(nums)
        # nums.sort() # to remove the duplicate subsets e
        def backtrack(path , i):
            ans.add(tuple(sorted(path.copy())))
            for sam in range(i , n):
                path.append(nums[sam])
                backtrack(path , sam+1)
                path.pop()

        backtrack([] , 0)
        return [list(subsets) for subsets in ans]



