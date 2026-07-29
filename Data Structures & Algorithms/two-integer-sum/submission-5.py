class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            rem = target - num
            lookup = seen.get(num, -1)
            if lookup != -1:
                return [seen[num], i]
            seen[rem] = i
            