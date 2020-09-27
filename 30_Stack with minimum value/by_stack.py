# first parameter is element, which stands for current element
# second parameter is min_val, which stands for global minimum value of stack

from collections import namedtuple
Entry = namedtuple('Entry', 'element min_val')


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [ ]
        
        

    def push(self, x: int) -> None:
        
		# update current global minimum value
        cur_min = min( x, self.stack[-1].min_val ) if self.stack else x
		
		# push new pair to stack
        self.stack.append( Entry(x, cur_min) )

            
            
    def pop(self) -> None:
        
		# pop lastest pair from stack
        self.stack.pop()
        
        

    def top(self) -> int:
        
		# fetch latest element from stack
        return self.stack[-1].element

    
    
    def getMin(self) -> int:
        
		# fetch latest global minimum value from stack
        return self.stack[-1].min_val



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        minStack = MinStack()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)
        
        result = minStack.getMin() # return -3
        self.assertEqual(result, -3)

        minStack.pop()

        result = minStack.top()    # return 0
        self.assertEqual(result, 0)

        result = minStack.getMin() # return -2
        self.assertEqual(result, -2)


if __name__ == '__main__':

    unittest.main()        