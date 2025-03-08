# Definition for singly-linked list.
from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        # ガード節によるチェック
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # 全部値を取り出してソートして入れ直す
        # NOTE: もう少しきれいにかけそうだけど処理自体は速い
        vals = []
        head: ListNode | None = list1
        while head:
            vals.append(head.val)
            head = head.next
        head = list2
        while head:
            vals.append(head.val)
            head = head.next
        vals.sort()
        result = ListNode(vals.pop(0))
        pos = result
        while vals:
            pos.next = ListNode(vals.pop(0))
            pos = pos.next

        return result


if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4, next=None)))
    l2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4, next=None)))
    print(solution.mergeTwoLists(l1, l2))

    l3 = None
    l4 = None
    print(solution.mergeTwoLists(l3, l4))

    l5 = None
    l6 = ListNode(val=0, next=None)
    print(solution.mergeTwoLists(l5, l6))
