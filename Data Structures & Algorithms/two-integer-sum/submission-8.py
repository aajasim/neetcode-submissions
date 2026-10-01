class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        balance = {}
        for i in range(len(nums)):
            bal = target - nums[i]
            if balance.get(nums[i], -1) != -1:
                return [balance.get(nums[i]), i]
            else:
                balance[bal] = i