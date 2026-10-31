class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #use a set to store numbers
        #loop through input array
        #check if n in set , if not add, if yes return false
        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False #duplicate