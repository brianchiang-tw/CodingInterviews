class Solution:
    def cuttingRope(self, n: int) -> int:

        if n <= 3:
            return n-1

        const = 10**9 + 7
        quotient, remainder = divmod(n, 3)

        if remainder == 0:
            return ( 3 ** quotient ) % const
        
        elif remainder == 1:
            return ( 3 ** (quotient - 1) * 4 ) % const
        
        else:
            return ( 3 ** quotient * 2 ) % const



# n : the value of input

## Time Complexity: O( 1 )
#
# The overhead in time is the cost of arithmetic operation, which is of O( 1 )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for temporary varible, which is of O( 1 )


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