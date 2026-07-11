class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_ = {}
        for num in nums:
            count_[num] = count_.get(num, 0) + 1
            if count_[num] > 1:
                return True
        return False
        