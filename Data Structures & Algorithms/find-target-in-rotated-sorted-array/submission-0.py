class Solution:
    def search(self, nums: List[int], target: int) -> int:

        #define pointers
        l,r= 0, len(nums) -1
        
        #while loop
        while l<=r:
            #define midpoint
            m = (l+r)//2
            if target == nums[m]:
                return m
            
            #if in left sorter array
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m +1
                else:
                    r = m -1
            #if in right sorted array
            else:
                if target < nums[m] or target > nums[r]:
                    r = m -1
                else:
                    l = m +1
        return -1

    
        
        
        
        #twopointers
        #while loop l<=r
        #if sorted then left value < right return left pointer
        #if in left sorted portion check if target > mid or target > left vlaue then l pointer moves to right
        #if in right sorted array check if target< mid value or target > value at right then move r pointer to left
        #return indice