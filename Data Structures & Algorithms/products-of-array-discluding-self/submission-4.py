class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        c=0 #counter to find how many zero are in nums
        k=0 #Flag to check if there's at least one non-zero element
        #Step 1: Calculate the product of all non-zero numbers and count the number of zeros
        for p in nums:
            if p!=0: 
                k=1 #Set k to 1 if there is at least one non-zero element
                product = product * p #Multiplying non-zero elements together
            else:
                c += 1 #Counting the number of zeros
                continue
        r = []
        #Step 2: Generate the result array r
        for i in range(len(nums)):
            if (c >= 2): #Case 1: for 2 or more 0s everything becomes 0
                r.append(0)
            elif (c==1 and nums[i]!=0) or k==0: #Case 2.1: Only 1 '0' in array & current element is not 0
                r.append(0) #Product for non-zero elements will be zero
            elif nums[i] == 0: #Case 2.2: Only 1 '0' in array & current element is 0
                r.append(int(product)) #Product of all other numbers (non-zero)
            else: #Case 3: General case, no zeros in the array
               r.append(int(product/nums[i])) #Divide total product by current element
        return r