class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_ = {}
        for num in nums:
            count_[num] = count_.get(num, 0) + 1
        sorted_keys = sorted(count_, key=lambda item:count_[item], reverse=True)
        return sorted_keys[:k]


        