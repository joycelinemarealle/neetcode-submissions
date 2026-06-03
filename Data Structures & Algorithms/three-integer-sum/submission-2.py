class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        #sort
        nums.sort()
        
        #loop through list sorted
        for i, a in enumerate(nums):
            #skip duplicate if from second number same as previ
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            #two pointers from second value
            l, r = i + 1, len(nums) -  1

            while l < r:
                tripletSum = a + nums[l] + nums[r]

                if tripletSum > 0:
                    r -= 1
                elif tripletSum < 0:
                    l +=1
                else: #means sum is o then move pointers
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1 #skip the duplicate to allow pointer to move forward
        return res
                





        #array to store the triplets
        #sort 
        #loop through and use two pointers n^2
        #skip duplicate
        #check tripletSum > 0 move right pointer to left
        #check tripletSum < 0 move left pointer to right
        # if triple sum == 0 then return [num[i],num[j],num[k]
         #move pointer l-> r <-
         #skip duplicates while l< r num[l] == num[l-1] and l<r
         #time Big O(n2) loop thne loop again for two pointers
         #memorry Big O (1) constant splace for arrya