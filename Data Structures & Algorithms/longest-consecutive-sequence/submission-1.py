class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #convert list to set
        numsSet = set(nums)
        longest = 0
        
        for n in nums:
            #check no left number then start of sequence
            if (n -1) not in numsSet:
                length = 0 #start of sequence
                #check current number
                while( n + length) in numsSet:
                    length += 1
                longest = max(length, longest)
        return longest

        #convert nums to set O(1) look up
        #store longest, length for tracking
        #loop through number check if previous n-1 in set: if not then it is a new seq
        # while it has prev num track length
        #return max longest
