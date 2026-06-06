class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l , r = 0, len(heights)-1
        area = 0

        while l < r:
            currArea = (r-l)* min(heights[l], heights[r]) #area of rectanlge limited by mini heigth
            area = max(currArea, area) #get max area
            if heights[l] < heights[r]:
                l+=1
            elif heights[l] > heights[r]:
                r-=1
            else: #if same height move either
                r-=1
        return area

        #eg index 0, 1, index 1, 7 -->
        #constrains min limits area
        #return in max area l*w rectanlge( max widht)
        #track max so need area = 0
        #two pointer one left, one right
        #if current area 
        #for every l*w
        #check max (current or intila)
        #time 
        #memory
        