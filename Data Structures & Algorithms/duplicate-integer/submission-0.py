class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_ = {}
        for num in nums:
            count_[str(num)] = count_.get(str(num), 0) + 1
            if count_[str(num)] == 2:
                return True
        return False
        