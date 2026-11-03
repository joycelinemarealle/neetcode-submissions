class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #use divide and conquer
        #check midpoint
        #if midpoint < target focus on right side
        #if midpoint > target focus on left side
        #if same return m
        #if all conditions not met return -1


        l,r = 0, len(nums)-1
        
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+ 1
            else:
                r = m-1
        return -1
        