class Solution:
    def plus_one(self, digits: list[int]) -> list[int]:
        adds = []
        plus_one = 1

        while digits:
            num = digits.pop(-1)
            num += plus_one
            plus_one, q = divmod(num, 10)
            adds.append(q)
            # 桁上り確認
            if plus_one == 0:
                break

        # 全体の桁上り確認
        if plus_one != 0:
            adds.append(plus_one)

        while adds:
            digits.append(adds.pop(-1))

        return digits


if __name__ == "__main__":
    solution = Solution()
    print(solution.plus_one([1, 2, 3]))  # [1,2,4]
    print(solution.plus_one([4, 3, 2, 1]))  # [4,3,2,2]
    print(solution.plus_one([9]))  # [1,0]
    print(solution.plus_one([1, 9, 9]))  # [2,0,0]
    print(solution.plus_one([9, 9, 9]))  # [1,0,0,0]
    print(solution.plus_one([1, 8, 9]))  # [1,9,0]
