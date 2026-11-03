class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "}" : "{", "]":"["}

        for c in s:
            #if close brackets
            if c in closeToOpen:
                #check stack
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            #open brackets 
            else:
                stack.append(c)

        #check if stack empty we donot have a match   
        if not stack:
            return True
        else:
            return False
        

        
        #store closeToOpen in dictionary
        #use a stack to store open brackets
        #loop through string
        #if open i will add to stack
        #if loop through keys of dicclose check if stack not empty , check if top value of stack == value as c as charact
        #when all characters check if not stack empty then true, if stack not empty return False means no match