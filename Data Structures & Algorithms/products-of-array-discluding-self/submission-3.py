class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        c=0
        k=0
        for p in nums:
            if p!=0:
                k=1
                product = product * p
            else:
                c += 1
                continue
        r = []
        for i in range(len(nums)):
            if (c >= 2): 
                r.append(0)
            elif (c==1 and nums[i]!=0) or k==0:
                r.append(0)
            elif nums[i] == 0:
                r.append(int(product))
            else:
               r.append(int(product/nums[i]))
        return r