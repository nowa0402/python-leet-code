class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        # HashMapの方法
        # 現在の要素の補数（target から現在の要素を引いた値）が
        # すでにハッシュテーブル内に存在するか確認します。
        # もし補数が見つかれば、それが解となるため、すぐにインデックスを返します。
        hash_map: dict[int, int] = {}
        for index, num in enumerate(nums):
            n = target - num
            if hash_map.get(n) is None:
                hash_map[num] = index
            else:
                return [hash_map[n], index]

        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.two_sum([2, 7, 11, 15], 9))
    print(solution.two_sum([3, 2, 4], 6))
    print(solution.two_sum([3, 3], 6))
