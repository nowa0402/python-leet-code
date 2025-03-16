class Solution:
    def str_str(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    # 別解
    def str_str_2(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.str_str("sadbutsad", "sad"))
    print(solution.str_str("leetcode", "leeto"))
    print(solution.str_str_2("sadbutsad", "sad"))
    print(solution.str_str_2("leetcode", "leeto"))
