class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_que , ans = deque() , []
        for i in range(len(nums)):
            if i >= k and max_que[0] == nums[i - k]:
                max_que.popleft()
            while max_que and max_que[-1] < nums[i]:
                max_que.pop()
            max_que.append(nums[i])
            if i >= k-1:
                ans.append(max_que[0])
        return ans
        