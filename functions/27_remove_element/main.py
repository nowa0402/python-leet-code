class Solution:
    def remove_element(self, nums: list[int | str], val: int) -> int:
        current_len = len(nums)
        while True:
            try:
                nums.remove(val)
            except Exception:
                break
        diff_len = len(nums)
        for _ in range(0, current_len - diff_len):
            nums.append("_")
        return diff_len

    # 早くてメモリ効率も良い感じ
    def remove_element_2(self, nums: list[int], val: int) -> int:
        # nums = [...] にすると、元のリストを参照している他の変数には影響しない
        # nums[:] = [...] にすると、リストオブジェクト自体が更新されるため、
        # 他の変数も影響を受ける可能性がある
        nums[:] = [x for x in nums if x != val]
        return len(nums)

    # filter関数でやる
    def remove_element_3(self, nums: list[int], val: int) -> int:
        nums[:] = list(filter(lambda x: x != val, nums))
        return len(nums)


if __name__ == "__main__":
    solution = Solution()
    print(solution.remove_element([3, 2, 2, 3], 3))
    print(solution.remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))
    print(solution.remove_element_2([3, 2, 2, 3], 3))
    print(solution.remove_element_2([0, 1, 2, 2, 3, 0, 4, 2], 2))
