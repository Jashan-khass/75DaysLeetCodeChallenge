class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

def build_list(arr):
    dummy = ListNode()
    cur = dummy
    for x in arr:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next

def to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

s = Solution()

print(to_list(s.middleNode(build_list([1,2,3,4,5]))))
print(to_list(s.middleNode(build_list([1,2,3,4,5,6]))))