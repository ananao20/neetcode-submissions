class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #2 pointer approach
        #dictionary
        #key (first value) : value (index)
        #check if complement exists in dictionary
        d = defaultdict(list)
        for i, n in enumerate(nums):
            complement = target - nums[i]
            if complement in d:
                return [d[complement], i]

            d[n] = i