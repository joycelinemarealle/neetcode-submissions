class Solution:
#binary search using recursion
    def binary_search(self, l:int, r:int,nums: List[int], target: int ) -> int:
        if l>r:
            return -1 #no target
        m = (l+r)//2 #midpoint

        if nums[m] == target:
            return m
            #if midpoint less than target focus on left side
        elif nums[m] < target: 
            return self.binary_search(m+1, r, nums, target)
        else:
            return self.binary_search(l,m-1, nums, target)
        

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0,len(nums)-1, nums, target)




        #binary search
        #if no target retunr 1
        #mid point
        #recusion search(0,m+1)
        #if 
        