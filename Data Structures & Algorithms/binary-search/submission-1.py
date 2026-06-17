class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l,r = 0, len(nums)-1

        while l <=r:
            m = (r+l)//2 #half way of distance

            if nums[m] < target: #focus on right side
                l= m+1
            elif nums[m] > target: #focus on left
                r = m-1
            else:
                return m
        return -1
        #binary search divide and conquer
        #l,r pointeres
        #if midpont< target move left to right
        #if opp move right to left
        #if midpoint === target then return m
        