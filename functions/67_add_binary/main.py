class Solution:
    def add_binary(self, a: str, b: str) -> str:
        result = int(a) + int(b)
        # print(result)
        adds = []
        while True:
            result, mod = divmod(result, 10)
            # print(f"result:{result}, mod:{mod}")
            match mod:
                case 2:
                    result += 1
                    adds.append("0")
                    continue
                case 3:
                    result += 1
                    adds.append("1")
                    continue
                case _:
                    adds.append(str(mod))
            if result == 0:
                break

        add_str = ""
        while adds:
            add_str += adds.pop(-1)

        return add_str

    # 早いかつ一番キレイなやつ
    def add_binary_2(self, a: str, b: str) -> str:
        # print(bin(int(a, 2) + int(b, 2))) # 0b*****
        # intの第二引数にバイナリの種類を渡せるので2進数を10進数数値変換
        # 合計した10進数をbin関数で2進数化して、[2:]で0b部分を除外した結果を返す
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == "__main__":
    solution = Solution()
    print(solution.add_binary("11", "1"))  # 100
    print(solution.add_binary("1010", "1011"))  # 10101
    print(solution.add_binary("1111", "1111"))  # 11110
    print(solution.add_binary_2("1111", "1111"))  # 11110
