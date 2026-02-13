class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0

        current = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                current += 1
            else:
                max_len = max(max_len, current)
                current = 1
        max_len = max(max_len, current)

        def two_letter(x, y):
            count_x = count_y = 0
            diff_map = {0: -1}
            res = 0

            for i, char in enumerate(s):
                if char == x:
                    count_x += 1
                elif char == y:
                    count_y += 1
                else:
                    count_x = count_y = 0
                    diff_map = {0: i}
                    continue

                diff = count_x - count_y
                if diff in diff_map:
                    res = max(res, i - diff_map[diff])
                else:
                    diff_map[diff] = i
            return res

        max_len = max(max_len,
                      two_letter('a', 'b'),
                      two_letter('a', 'c'),
                      two_letter('b', 'c'))

        count_a = count_b = count_c = 0
        diff_map = {(0, 0): -1}

        for i, char in enumerate(s):
            if char == 'a':
                count_a += 1
            elif char == 'b':
                count_b += 1
            else:
                count_c += 1

            key = (count_a - count_b, count_a - count_c)

            if key in diff_map:
                max_len = max(max_len, i - diff_map[key])
            else:
                diff_map[key] = i

        return max_len
