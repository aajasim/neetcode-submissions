class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        targets = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            rem_check = targets.get(rem, -1)
            if rem_check == -1:
                targets[nums[i]] = i
            else:
                return [rem_check, i]
        
        