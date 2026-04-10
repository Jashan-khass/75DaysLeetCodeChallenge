class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

def create_list(values, pos):
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(values) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]

s = Solution()

head1 = create_list([3,2,0,-4], 1)
print(s.hasCycle(head1))

head2 = create_list([1,2], 0)
print(s.hasCycle(head2))

head3 = create_list([1], -1)
print(s.hasCycle(head3))