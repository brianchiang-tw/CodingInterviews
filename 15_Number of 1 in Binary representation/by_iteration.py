class Solution:
    def hammingWeight(self, n: int) -> int:

        # count the 1s by bit masking in generator expression
        return sum(  1 for i in range(32) if ( (n >> i) & 1 )  )



## Time Complexity: O( 1 )
#
# The overhead in time is the cost of generator expression, which is of O( 32 ) = O( 1 )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 ) 


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().hammingWeight( int("00000000000000000000000000001011", 2) ) 
        self.assertEqual( result, 3)


    def test_case_2( self ):

        result = Solution().hammingWeight( int("00000000000000000000000010000000", 2) ) 
        self.assertEqual( result, 1)


    def test_case_3( self ):

        result = Solution().hammingWeight( int("11111111111111111111111111111101", 2) ) 
        self.assertEqual( result, 31)


if __name__ == '__main__':

    unittest.main()