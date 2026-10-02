class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for c in range(0, len(nums)):
            if target - nums[c] in d:
                return [d[target - nums[c]], c]
            else:
                d[nums[c]] = c
