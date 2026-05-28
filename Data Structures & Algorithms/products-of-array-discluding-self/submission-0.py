class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1]* (len(nums)) #array of length as list
        prefix = 1
        for i in range(len(nums)): #from start to end
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range (len(nums)-1, -1, -1): #from end to start
            res[i] *= postfix #if = replacing all prefix
            postfix *= nums[i]
        return res

        #time Big O (2n)
        #memory space Big O(n) stored in array
        #loop through. store prefixxi and postfix
        #lopp to store prefix
        #loop multip with psotfix
        #return array with result
        

        