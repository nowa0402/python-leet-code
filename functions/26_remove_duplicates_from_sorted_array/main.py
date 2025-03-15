class Solution:
    # このやり方でも良いはずではあるが、numsに破壊的変更が加えられないため駄目っぽい
    def remove_duplicates(self, nums: list[int | str]) -> int:
        current_nums_len = len(nums)
        nums = list(dict.fromkeys(nums))
        result = len(nums)
        for _ in range(0, current_nums_len - result):
            nums.append("_")
        print(nums)
        return result

    # 正攻法
    def remove_duplicates_2(self, nums: list[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j


if __name__ == "__main__":
    solution = Solution()
    print(solution.remove_duplicates([1, 1, 2]))
    print(solution.remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
