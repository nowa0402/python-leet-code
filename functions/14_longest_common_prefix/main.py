class Solution:
    def longest_common_prefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        base = strs.pop(0)
        for s in strs:
            while True:
                if s.startswith(base):
                    break
                base = base[:-1]
                if base == "":
                    return base
        return base

    # 別解：ソートした後に最小値と最大値で比較する。
    # メモリ効率はこっちのほうが良い。速さはLeetCode上はどちらでも同じ速度
    def longest_common_prefix_2(self, strs: list[str]) -> str:
        ans = ""
        v = sorted(strs)
        first = v[0]
        last = v[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]
        return ans


if __name__ == "__main__":
    solution = Solution()
    assert solution.longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert solution.longest_common_prefix(["dog", "racecar", "car"]) == ""
    assert solution.longest_common_prefix_2(["flower", "flow", "flight"]) == "fl"
    assert solution.longest_common_prefix_2(["dog", "racecar", "car"]) == ""
