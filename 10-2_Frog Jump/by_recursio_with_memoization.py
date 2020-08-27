class Solution:
    def numWays(self, n: int) -> int:

        memo = { 0: 1, 1: 1 }

        # ------------------------------------------------
        def jump(n):

            if n in memo:
                return memo[n]

            else:

                jump_method = jump(n-1) + jump(n-2)
                memo[n] = jump_method
                return jump_method

        # ------------------------------------------------

        return jump(n) % ( 10**9 + 7 )




# n : the value of input

## Time Complexity: O( n )
#
# The overhead in time is the cost of recursion with memoization, which is of O( n )

## Space Comlexity: O( n )
#
# The overhead in space is the storage for recursion call stack as well as memoization table, which is of O( n )



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().numWays(0)
        self.assertEqual(result, 1)



    def test_case_2( self ):

        result = Solution().numWays(1)
        self.assertEqual(result, 1)       


    def test_case_3( self ):

        result = Solution().numWays(9)
        self.assertEqual(result, 55)   


if __name__ == '__main__':

    unittest.main()                