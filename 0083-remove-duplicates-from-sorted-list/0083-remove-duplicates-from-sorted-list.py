class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head

def build_linked_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next

def linked_list_to_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result

test_cases = [
    [1, 1, 2],
    [1, 1, 2, 3, 3]
]

solution = Solution()

for case in test_cases:
    head = build_linked_list(case)
    new_head = solution.deleteDuplicates(head)
    print("Input:", case)
    print("Output:", linked_list_to_list(new_head))
    print()