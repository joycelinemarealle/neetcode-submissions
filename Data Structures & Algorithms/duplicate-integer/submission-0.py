class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = set()
        for num in nums:
            if num in dups:
                return True
            else:
                dups.add(num)
        return False

        #add a set
        #go through array
        #if it is return false
        #each check if value in dic if not add count
        #return true after loop
        #Big o Big (o) + n -> Big (0) memory dict n + m (array and dictionary)
        
        