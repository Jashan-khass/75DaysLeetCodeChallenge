class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return head
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        first, second = head, prev
        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first, second = t1, t2
        return head

def build(arr):
    dummy = ListNode()
    cur = dummy
    for x in arr:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next

def show(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

cases = [
    [1,2,3,4],
    [1,2,3,4,5]
]

for c in cases:
    h = build(c)
    Solution().reorderList(h)
    print("input:", c, "output:", show(h))