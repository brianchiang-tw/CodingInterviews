class CQueue:

    def __init__(self):

        # buffer for element input
        self.in_stack = []

        # buffer for element output
        self.out_stack = []



    def appendTail(self, value: int) -> None:

        self.in_stack.append(value)



    def deleteHead(self) -> int:

        if not self.out_stack:
            # dump all elements from in_stack to out_stack
            while self.in_stack:
                self.out_stack.append( self.in_stack.pop() )
        
        if not self.out_stack:
            # if out_stack is still empty, then this queue is empty.
            return -1

        else:
            return self.out_stack.pop()