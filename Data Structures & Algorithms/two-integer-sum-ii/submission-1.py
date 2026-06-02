class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r:
            curSum = numbers[l] + numbers[r]
            
            if curSum > target:
                r -= 1 #shift right pointer left to decrease sun
            elif curSum < target:
                l += 1 #shift left point right toincrease sum
            else: #if target same as sum return index
                return [l + 1, r + 1 ] #index are +1 normal
              
           
           
           
            # complements = {}
            # for i, n in enumerate(numbers):
            #     complement = target - n
            #     if (target - n) not in complements:
            #         complements[complement] = i+1
            #     else:
            #         return list([i+1, complements[complement]])
            

        #array sorted
        #two pointers beginning and end
        #check sum if > target shift p=right point left if targe< then shigh left pointer right
        
        #nope
        #loop throughe enumerate
        #check complement in set
        #if not add
        #if yes return indeces
        #binary search if value  , target
        #if value > target mid the upper rigth