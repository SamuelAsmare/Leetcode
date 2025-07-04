class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left , right , ans  = 0 , len(people)-1 , 0
        while(right>=left):
            if people[right] + people [left] <= limit:
                ans += 1
                left += 1
                right -=1
            else:
                ans += 1
                right -= 1
        return ans

            
