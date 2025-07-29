class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
                return []
        intervals.sort(key=lambda x: x[0])

        merg = [intervals[0]]

        for current in intervals[1:]:
            last = merg[-1]

            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                merg.append(current)

        return merg