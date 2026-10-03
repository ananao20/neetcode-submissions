class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        maxl, curr = 1,1
        for c in s:
            if c-1 not in s:
                n = c
                cnt = 1
                while n+1 in s:
                    cnt+=1
                    n+=1
                maxl = max(maxl, cnt)
        return maxl

