class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        #Iterate through array and skip duplicate
        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            #Iterate using two pointers
            l,r = i+1, len(nums)-1
            
            while l < r:
                sum_ = n + nums[l]+ nums[r]
                #sum_ conditions
                if sum_ < 0:
                    l+=1
                elif sum_ > 0:
                    r-=1
                else:
                    res.append([n,nums[l],nums[r]])
                    l+=1 #move pointer since other triples possible
                    r-=1
                    #make sure duplicate are skipped when pointers move
                    while l<r and nums[l] == nums[l-1]: 
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
        return res

  #sort to use pointers
        #Iterate through array skip if duplicate
        #Loop and useTwo pointers. Left and right
        # if sum = 0 return indices + move pointers
        #if sum > 0 decrement r
        #if sum < 0 increment l
