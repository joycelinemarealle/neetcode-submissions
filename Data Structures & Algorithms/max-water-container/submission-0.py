class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #Two pointers
        #left , right
        #while l<r iterate array
        # areas,  max(min height * width)
        #move left pointer if height is smaller
        # move right point if its height is smaller

        l,r = 0, len(heights)-1
        max_area = 0

        #Iterate through input array
        while l < r:
            area = min (heights[l], heights[r]) * (r-l)
            max_area = max(area, max_area)

            if heights[l] <= heights[r]:
                l +=1
            else:
                r -=1
        return max_area
        