import heapq

class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)

        return self.heap[0]


kthLargest = KthLargest(3, [4, 5, 8, 2])

print(kthLargest.add(3))
print(kthLargest.add(5))
print(kthLargest.add(10))
print(kthLargest.add(9))
print(kthLargest.add(4))

kthLargest2 = KthLargest(4, [7, 7, 7, 7, 8, 3])

print(kthLargest2.add(2))
print(kthLargest2.add(10))
print(kthLargest2.add(9))
print(kthLargest2.add(9))