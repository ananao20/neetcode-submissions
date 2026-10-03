class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = list(sorted(set(nums)))
        maxl, curr = 1,1
        for c in range(0, len(s)-1):
            if s[c]+1==s[c+1]:
                curr+=1
                maxl=max(maxl,curr)
            else:
                curr=1
        return maxl

