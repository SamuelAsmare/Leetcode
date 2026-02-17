class Solution:
    def readBinaryWatch(self, t: int) -> List[str]:
        ans = []
        for h in range(12):
            for m in range(60):
                if bin(h).count("1") + bin(m).count("1") == t:
                    ans.append(f"{h}:{m:02d}")

        return ans
