class MinStack:

    def __init__(self):
        #define 2 stacks
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        #if not empty add min to minStack else just add val
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

        #use stack pop, top O(1)
        #min stack i will store as i add new value the min at the moment, then return the top of minstack
        #to push append in arraylisy
        #top very last in stack [-1]
        
