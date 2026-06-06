class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        #sorted
        nums.sort()
        
        #-4,-1,-1,0,1,2
        #[0,1,1]
        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]: #skip duplocates
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r -=1
                elif threeSum < 0:
                    l +=1
                else: 
                    res.append([nums[i], nums[l], nums[r]])
                    #move pointers
                    l+=1
                    r-=1
                    #skip duplicates
                    while l <r and nums[l] == nums[l-1]:
                        l +=1
                    while l<r and nums[r] == nums[r+1] :
                        r-=1
        return res

        #constrains no duplicates.. triplest unique
        #input integers, output, 3 triplets
        #ordered? nope, order does not mater
        #array to hold indices res [] =--> [[],[]]
        #two pointers
        #not sored sort first
        #looping then anothe rloop use twopointer form the next idnexi
        #if thressSUM > 0 move right to left , < 0 move left to right
        #if == 0 then return the numebrs res.appendp[[],[],[]]
        #time Bi O(n^2)
        #memory res[] big O(1 ) constant
        