

class Solution:
    def cuttingRope(self, n: int) -> int:

        if n <= 3:
            return n-1

        result = 1
        while n > 4:
            result *= 3
            n -= 3
        
        return result * n


# n : the value of input

## Time Complexity: O( n )
#
# The overhead in time is the cost of while-loop, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )


import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().cuttingRope( n=2 )
        self.assertSetEqual( result, 2)

    
    def test_case_2( self ):

        result = Solution().cuttingRope( n=3 )
        self.assertEqual( result, 2)


    def test_case_3( self ):

        result = Solution().cuttingRope( n=10 )
        self.assertEqual( result, 36)


if __name__ == '__main__':

    unittest.main()                