class Solution:
    def fib(self, n: int) -> int:
        
        # create memoization table with base case
        # f(0) = 0
        # f(1) = 1
        memo = {0: 0, 1: 1}

        def f(n: int) -> int:

            if n in memo:
                return memo[n]
            
            result = f(n-1) + f(n-2)

            # update memoization table
            memo[n] = result
            return result

        return f(n) % (10**9 + 7)



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

        result = Solution().fib(0)
        self.assertEqual(result, 0)



    def test_case_2( self ):

        result = Solution().fib(1)
        self.assertEqual(result, 1)       


    def test_case_3( self ):

        result = Solution().fib(10)
        self.assertEqual(result, 55)   


if __name__ == '__main__':

    unittest.main()        