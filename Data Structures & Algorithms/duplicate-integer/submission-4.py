class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Sol 1:
        # d = set(nums)
        # if len(d)==len(nums): 
        #     return False
        # else: 
        #     return True
        #########
        #Sol 2:
        a = {}
        for c in nums:
            if c in a:
                return True
            else:
                a[c]=1
        return False
        
        