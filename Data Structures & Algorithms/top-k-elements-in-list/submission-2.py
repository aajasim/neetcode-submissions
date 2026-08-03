class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_ = {}
        for num in nums:
            counter_[num] = counter_.get(num, 0) + 1
        sorted_dic = dict(sorted(counter_.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_dic.keys())[:k]