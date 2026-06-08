class Solution:
    def trap(self, height: List[int]) -> int:
        #constraint
        if not height:
            return 0 #if height[i] does not exist
        
        #Two pointers
        l,r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0 #to track water squares
        while l < r:
            if leftMax < rightMax:
                l+=1
                leftMax = max(leftMax, height[l])
                res += leftMax-height[l]
            else:
                #move pointer
                r-=1
                #update tracked rightMax
                rightMax = max(rightMax, height[r])
                res += rightMax-height[r]
        return res


        #water at each poistion = is max wall on that side - height at that position
        #two pointers
        #water trapped limited to min left. if left < right we move pointer or min right
        #track left max, rightmax
        #wile left pont. < right pointer
        #move pointer, update leftmax, add square to result leftMax-height[i]
        #else move r to legt , update right max, update result