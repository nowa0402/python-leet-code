class Solution:
    def length_of_last_word(self, s: str) -> int:
        strs = [len(word) for word in s.split(" ") if word]
        return strs.pop(-1)

    def length_of_last_word_2(self, s: str) -> int:
        stack_s: list[str] = []
        for i in reversed(s):
            if i == " ":
                if len(stack_s) != 0:
                    break
                else:
                    continue
            stack_s.append(i)
        return len(stack_s)


if __name__ == "__main__":
    solution = Solution()
    print(solution.length_of_last_word("Hello World"))
    print(solution.length_of_last_word("   fly me   to   the moon  "))
    print(solution.length_of_last_word("luffy is still joyboy"))
    print(solution.length_of_last_word("Today is a nice day"))
    print("=====")
    print(solution.length_of_last_word_2("Hello World"))
    print(solution.length_of_last_word_2("   fly me   to   the moon  "))
    print(solution.length_of_last_word_2("luffy is still joyboy"))
    print(solution.length_of_last_word_2("Today is a nice day"))
