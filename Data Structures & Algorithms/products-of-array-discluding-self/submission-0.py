class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            pdt = 1
            for j in range(len(nums)):
                if i==j:
                    continue
                else:
                    pdt = pdt * nums[j]
            result.append(pdt)
        return result
