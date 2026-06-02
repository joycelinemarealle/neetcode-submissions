class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numsSet = set(nums)
        longest = 0 #keep track of longesth consecutive length
       
        for n in nums:
            if n-1 not in numsSet:
                length = 0 #beginnign of a sequence no previous value eg 2 no 1
                while(n + length) in numsSet:
                    length +=1 #keep on adding streak as long as consecutive +1 in numsset
                longest = max(length, longest)
        return longest



        
        #have a set easy look O(1)
        #keep track. of longest
        #loop through list
        #check if num has no num before it in set
        #if no length o begining of a sequence
        # keep on adding streak as long as num+length in set
        #keep on adding until not then move to next nums
        #return max length