class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]
        for i in range(len(candies)):
            candies[i]=candies[i]+extraCandies
            ans.append(candies[i]==max(candies))
            candies[i]=candies[i]-extraCandies
        return ans


                