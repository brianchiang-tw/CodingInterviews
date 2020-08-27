class Solution:
    def fib(self, n: int) -> int:

        if n <= 1:
            return n
            
        f_n_2, f_n_1 = 0, 1

        f_n = -1
        for i in range(2, n+1):

            # compute f(n) = f(n-2) + f(n-1)
            f_n = f_n_2 + f_n_1
            
            # update f(n-2) and f(n-1) as f(n-1) and f(n)
            f_n_2, f_n_1 = f_n_1, f_n

        return f_n % (10**9 + 7)



# n : the value of input

## Time Complexity: O( n )
#
# The overhead in time is the cost of for-loop iteration, which is of O( n )

## Space Comlexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )



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