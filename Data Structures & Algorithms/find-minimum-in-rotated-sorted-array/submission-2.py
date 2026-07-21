class Solution:
    def findMin(self, nums: List[int]) -> int:

        #pointers
        res = nums[0] #need starting value pick any valu
        l,r = 0, len(nums)-1

        #loop aslong pointer valid position
        while l <= r:
        #edge case if subarray already sorted then  assign min res, m
            if nums[l] < nums[r]:
                #update res
                res = min(res,nums[l])
                break #break out of loop
    #if not sorted
            m = (l + r) // 2
            res = min(res,nums[m])
            #move r pointer if have left sorted array search right side
            if nums[m] >= nums[l]: #means left sorted array
                l = m+1
            else: #if in right sorted portion want to search left
                r = m-1
        
        return res
        


        #Two pointers
        # track min value res[]
        #loop while l<=r valid position
        #edge if left value  < right value midpoint set min of res , left
         #if mid valu > than further right means dealing with left sorted so move left to right
        #if mid value< than further left then dealing with right so move right to left
        #return res
        