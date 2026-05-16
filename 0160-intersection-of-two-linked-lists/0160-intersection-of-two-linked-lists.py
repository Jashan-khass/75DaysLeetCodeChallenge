class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        a, b = headA, headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a


def build_intersected_lists(listA, listB, skipA, skipB):
    nodesA = [ListNode(v) for v in listA]
    nodesB = [ListNode(v) for v in listB]

    for i in range(len(nodesA) - 1):
        nodesA[i].next = nodesA[i + 1]

    for i in range(len(nodesB) - 1):
        nodesB[i].next = nodesB[i + 1]

    if skipA < len(nodesA) and skipB < len(nodesB):
        intersect = nodesA[skipA]
        nodesB[skipB] = intersect

        if skipB > 0:
            nodesB[skipB - 1].next = intersect

    return nodesA[0], nodesB[0]


headA1, headB1 = build_intersected_lists(
    [4, 1, 8, 4, 5],
    [5, 6, 1, 8, 4, 5],
    2,
    3
)

headA2, headB2 = build_intersected_lists(
    [1, 9, 1, 2, 4],
    [3, 2, 4],
    3,
    1
)

a1 = ListNode(2)
a1.next = ListNode(6)
a1.next.next = ListNode(4)

b1 = ListNode(1)
b1.next = ListNode(5)

sol = Solution()

result1 = sol.getIntersectionNode(headA1, headB1)
print("Example 1:", result1.val if result1 else "No intersection")

result2 = sol.getIntersectionNode(headA2, headB2)
print("Example 2:", result2.val if result2 else "No intersection")

result3 = sol.getIntersectionNode(a1, b1)
print("Example 3:", result3.val if result3 else "No intersection")