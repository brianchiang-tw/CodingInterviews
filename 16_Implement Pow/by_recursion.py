class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1

        elif n < 0:
            return 1 / self.myPow(x, -n)

        else:

            if n % 2 == 0:
                return self.myPow(x*x, n//2)
            else:
                return self.myPow(x*x, n//2) * x



# n : the value of input parameter n

## Time Complexity: O( log n )
#
# The overhead in time is the cost of fast power, which is of O( log n )

## Space Complexity: O( log n )
#
# The overhead in space is the storage for recursion call stack, which is of O( log n)


import unittest
from math import isclose

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().myPow(2, 10)
        self.assertEqual( result, 1024.0)
        
    
    def test_case_2( self ):

        result = Solution().myPow(2, -10)
        self.assertEqual( result, 1.0 / 1024.0 )

    
    def test_case_3( self ):

        result = Solution().myPow(2, 0)
        self.assertEqual( result, 1.0 )


    def test_case_4( self ):

        result = Solution().myPow(2.1, 3)
        self.assertEqual( isclose(result, 9.261), True )


    def test_case_5( self ):

        result = Solution().myPow(2.0, -2)
        self.assertEqual( result, 0.25 )


if __name__ == '__main__':

    unittest.main()        


