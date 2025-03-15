from collections import deque


class Solution:
    def is_valid(self, s: str) -> bool:
        hash_maps = {
            "{": "}",
            "(": ")",
            "[": "]",
        }
        if len(s) % 2 == 1:
            return False

        q: deque[str] = deque([])
        for c in s:
            if len(q) == 0:
                q.append(c)
                continue

            if hash_maps.get(c):
                q.append(c)
                continue

            if c != hash_maps.get(q.pop()):
                return False

        return True if len(q) == 0 else False

    # 別解。こっちのほうがきれい
    def is_valid_2(self, s: str) -> bool:
        mapping = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        stack = []

        for paren in s:
            if paren in mapping:
                stack.append(paren)
            elif paren not in mapping and stack:
                top_of_stack = stack.pop()
                if mapping[top_of_stack] != paren:
                    return False
            else:
                return False

        return not stack


if __name__ == "__main__":
    solution = Solution()
    assert solution.is_valid("()") is True
    assert solution.is_valid("()[]{}") is True
    assert solution.is_valid("(]") is False
    assert solution.is_valid("([])") is True
