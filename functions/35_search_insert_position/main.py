class Solution:
    def search_insert(self, nums: list[int], target: int) -> int:
        nums.append(target)
        nums.sort()
        return nums.index(target)

    def search_insert_2(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    solution = Solution()
    print(solution.search_insert([1, 3, 5, 6], 5))  # 2
    print(solution.search_insert([1, 3, 5, 6], 2))  # 1
    print(solution.search_insert([1, 3, 5, 6], 7))  # 4
    print(solution.search_insert([1, 3], 3))  # 1
    print(solution.search_insert([1, 4, 6, 7, 8, 9], 6))  # 2
    print(solution.search_insert([1, 3, 5], 4))  # 2
    print("=====")
    print(solution.search_insert_2([1, 3, 5, 6], 5))  # 2
    print(solution.search_insert_2([1, 3, 5, 6], 2))  # 1
    print(solution.search_insert_2([1, 3, 5, 6], 7))  # 4
    print(solution.search_insert_2([1, 3], 3))  # 1
    print(solution.search_insert_2([1, 4, 6, 7, 8, 9], 6))  # 2
    print(solution.search_insert_2([1, 3, 5], 4))  # 2
