class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pr = 1
        f = 0
        for c in nums:
            if c!=0 and f!=2 :
                pr = pr*c
            elif f<2:
                f += 1
        if f>1:
            return [0]*len(nums)
        ans = [0]*len(nums)
        for c in range(0,len(nums)):
            if f!=1:
                ans[c] = int(pr/nums[c])
                # ans[c] = pr//nums[c]
            else:
                if nums[c]==0:
                    ans[c]=pr
                else:
                    ans[c]=0
        return ans
