from collections import defaultdict

class Solution:
    def cuttingRope(self, n: int) -> int:
        
        if n == 1:
            # can not make a cut
            return 1
        
        elif n == 2 or n == 3:
            
            # 2 = 1 + 1, product = 1 x 1 = 1
            # 3 = 2 + 1, product = 2 x 1 = 2
            return (n-1)
        
        
        # key: interger
        # value: max product of integer break
        dp = defaultdict(int)
        
        # base case:
        for i in range(0, 5):
            dp[i] = i
        
        # general case:
        for i in range(5, n+1):
            
            for j in range(i//2+1):
                
                dp[i] = max(dp[i], dp[j] * dp[i-j])
                
        
        return dp[n]



# n : the value of input

## Time Complexity: O( n^2 )
#
# The overhead in time is the cost of nested loops, which is of O( n ^ 2)

## Space Complexity: O( n )
#
# The overhead in space is the storage for dp table, which is of O( n )


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