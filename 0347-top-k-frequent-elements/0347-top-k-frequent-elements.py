class Solution:
    def topKFrequent(self, nums, k):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

obj = Solution()
print(obj.topKFrequent([1,1,1,2,2,3], 2))
print(obj.topKFrequent([1], 1))
print(obj.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))
print(obj.topKFrequent([5,5,5,5], 1))
print(obj.topKFrequent([1,2,3,4], 2))
print(obj.topKFrequent([-1,-1,-2,-2,-2,-3], 2))