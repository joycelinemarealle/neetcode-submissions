class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False

        #big O( n) time complexity
        #space big(1) constant
        
        #set to save tracked num in numa
        #loop through num in nums
        #if in set , add it set True- duplicate
        #if not set then add it --> function return False
        #input intege, output true.false
        #will i always duplicates no 