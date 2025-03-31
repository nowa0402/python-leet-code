# Definition for singly-linked list.
from __future__ import annotations

from pprint import pprint as print


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


class Solution:
    # 自分の回答
    # def delete_duplicates(self, head: ListNode | None) -> ListNode | None:
    #     if head is None:
    #         return None
    #     prev = head
    #     current = head.next

    #     while current:
    #         if prev.val == current.val:
    #             prev.next = current.next
    #             current = current.next
    #         else:
    #             prev = prev.next  # type: ignore
    #             current = current.next
    #     return head

    # 模範解答
    # やっていることは自分の回答と一緒だが、変数が少ない分効率的
    def delete_duplicates_2(self, head: ListNode | None) -> ListNode | None:
        res = head

        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return res


if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(val=1, next=ListNode(val=1, next=ListNode(val=2, next=None)))
    l2 = ListNode(
        val=1,
        next=ListNode(
            val=1,
            next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=3, next=None))),
        ),
    )
    print(solution.delete_duplicates_2(l1))  # [1,2]
    print(solution.delete_duplicates_2(l2))  # [1,2,3]
