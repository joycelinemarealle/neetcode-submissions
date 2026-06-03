class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #Time Big O(n)

        l , r = 0, len(heights) -1
        res = 0 # initialize to track max area

        while l < r:
            area = (r-l) * min( heights[l],heights[r])
            res = max(res, area)

            #to change pointers
            if heights[l] < heights[r]:
                l +=1

            elif heights[r] < heights[l]:
                r -=1
            else: #when heights same move either
                r -=1
        return res
            



        
        #Brute Force
        res = 0 # initial area
        for l in range(len(heights)):
            for r in range( l+1, len(heights)):
                area = (r-l) * min(heights[l], heights[r])
                res = max(res,area)
        return res


        #two pointer
        # have l, and r pointers
        # if height[l] < height[r]: move pointer left to right
        # if height[r] <>height[l]: move pointer right to left
        #if same then move pointers r-=1 just one of 
        # return max

        #bruteforce big O (n^2)
        #loop through heights
        # nested loop
        #check area = diff of l+r  * min of height
        #track max area
        #return area
        #time big O (n ^2)
        #mem big O (1)
        