class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        m, n = len(nums1), len(nums2)

        for i in range(m):
            l, r = i, n - 1

            while l <= r:
                mid = (l + r) // 2
                if nums2[mid] >= nums1[i]:
                    ans = max(ans, mid - i)
                    l = mid + 1
                else:
                    r = mid - 1
        return ans