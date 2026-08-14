class Solution:
    def isValid(self, s: str) -> bool:


        #key to val pairs closer:opener
        pairs = {')':'(', '}':'{', ']':'[' }
        stack = []

        for ch in s:
            #adding opener to stack {
            if ch not in pairs:
                stack.append(ch)
            
            #if closer }
            else:
                if not stack:
                    return False
                
                if stack[-1] != pairs[ch]:
                    return False
           
                #discard from stack if pair found {}
                stack.pop() 
        
        #invalid if there are left overs
        return len(stack) == 0

         
        
        #keepy track of closer:opener key:value
        #loop through left to right in s
        #add openers to stack if  opener add to stack, if closer then check stakc empty or invalid pair
        #innermost top of stack will be pair then pop so discard
        #return  len of stack is zero true
        #