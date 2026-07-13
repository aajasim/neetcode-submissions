class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        balance = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if balance.get(nums[i], -1) != -1:
                return [balance.get(nums[i], -1), i]
            if balance.get(rem, -1) != -1:
                continue
            else:
                balance[rem] = i
            