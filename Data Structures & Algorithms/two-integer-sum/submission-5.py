class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        for i, num in enumerate(nums):
            complement = target-num

            if complement in seen:
                return [seen[complement],i]
            #add indice
            seen[num] = i
                

        

        #dic to keep track fo complement
        #loop through and add compleemt in dic
        #if complement seen then return the indices

        