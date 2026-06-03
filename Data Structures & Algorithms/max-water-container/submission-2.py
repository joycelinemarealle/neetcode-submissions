class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #brute force
        res = 0 # initial area
        for l in range(len(heights)):
            for r in range( l+1, len(heights)):
                area = (r-l) * min(heights[l], heights[r])
                res = max(res,area)
        return res


        #bruteforce big O (n^2)
        #loop through heights
        # nested loop
        #check area = diff of l+r  * min of height
        #track max area
        #return area
        #time big O (n ^2)
        #mem big O (1)
        