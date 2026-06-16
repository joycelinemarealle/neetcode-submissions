class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        #loop throught string andto see if operator, if not add to stack
        for c in tokens:
            #pop two then do operator
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                #order matters
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                #order matters
                a,b = stack.pop(), stack.pop()
                stack.append(int(b/a)) #round to zero
            else:
                stack.append(int(c)) #convert char to int

        return stack[0]

        #check if operator then pop and do operation(if,elif, else means non operator it is numeric)
        #-, / want to take popped of last then pop second last
        #big O(n)
        #memory stack bigO(1)