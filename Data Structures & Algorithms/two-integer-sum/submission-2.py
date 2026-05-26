class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement],i] #found match
            #add indice
            seen[num] = i 


        #always be atleast one pair? dupicate as long meet target? order of retun of indices
        #dictionary key complement as i loop t + value indice
        #loop through array
        # if complement seen then return indices []
        #if not store it - add indice for complement
        #Time Big O(n) looping through array
        #Memory Big O(1) constant space
        