class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        res = 0 #track max count once zero is seent
        cnt = 0 #keep track of consecutive 1's

        for num in nums:
            if num == 0:
                res = max(res,cnt)
                cnt = 0
            else:
                cnt += 1
        return max(cnt, res)

       
       
        #Solution
        #loop through each element in array
        #if num in nums == 0 update return max res,cnt then initialize count to zero and 
        #else if one then increase count by 1
        #Time Big O(n), Space Big O(1)


        