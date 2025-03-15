class Solution:
    def is_palindrome(self, x: int) -> bool:
        if x < 0:
            return False

        num_list = []
        n = x
        while n > 9:
            num_list.append(n % 10)
            n = int(n / 10)
        num_list.append(n)

        for count in range(0, int(len(num_list) / 2)):
            first = num_list[count]
            last = num_list.pop()
            if first != last:
                return False

        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.is_palindrome(121))
    print(solution.is_palindrome(-121))
    print(solution.is_palindrome(10))
