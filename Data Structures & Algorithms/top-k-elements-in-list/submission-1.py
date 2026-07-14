class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
        sorted_ = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_.keys())[:k]

        