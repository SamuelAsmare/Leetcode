class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        stack,size=[],len(nums)
        while(size>0):
            alice=min(nums)
            nums.remove(alice)
            bob=min(nums)
            nums.remove(bob)
            stack.append(bob)
            stack.append(alice)
            size-=2
        return stack