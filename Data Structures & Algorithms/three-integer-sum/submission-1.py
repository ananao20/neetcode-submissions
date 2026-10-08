class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        if nums[0]>0:
            return []
        ans = []
        i=0
        while i<len(nums)-2:
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k]<0:
                    j+=1
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                else:
                    if [nums[i],nums[j],nums[k]] not in ans:
                        ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
            i+=1
        return ans