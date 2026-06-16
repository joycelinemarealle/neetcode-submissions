class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #defaul array
        res = [0] * len(temperatures)
        stack = [] #pair [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd]= (i-stackInd)
            stack.append([t,i])
        return res



        #loop through temp for every temp check while stack not empty if greater than temp at top of stack
        #if greater take diff and pop , if not add temp to stack and continue looping
        #compare to top of stack if greater then pop
        #diff index eg [1] -[0] 1 steps
        #add result of idff at index on in loop
        #pop from stack
        #continue looping if not greater then add to stack, cant pop