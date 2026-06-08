class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #track opening brackes
        closeToOpen = {")": "(", "}":"{", "]": "["} #hashmap to store key:val close brackets:open

        #loop through string and check if any close
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                     stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

        
        #use stack to store open brackets have seen
        #use stakc Lifo last in first out
        #hashmap key,value close:open
        #loop through string if char in close then
        # if stack not emptyand last char == key has value = ( open then pop from stack
        #if empty add the
        #return True if stack empty
        #time Big O(n) too
        #memory Big O(n) stack