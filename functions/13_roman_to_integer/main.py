class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0
        prev = None
        # 文字列はforで回せば一文字ずつ取れる
        # 一旦リストにするのは時間がかかる
        # str_list = list(s)

        for i in s:
            num = roman_map[i]
            result += num

            # 初回
            if prev is None:
                prev = num
                continue

            # 組み合わせルールの適用
            if prev < num:
                result -= prev * 2

            prev = num

        return result

    # 別解。おしゃれ
    def romanToInt_2(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number


if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt("III"))
    print(solution.romanToInt("LVIII"))
    print(solution.romanToInt("MCMXCIV"))
    print(solution.romanToInt_2("III"))
    print(solution.romanToInt_2("LVIII"))
    print(solution.romanToInt_2("MCMXCIV"))
