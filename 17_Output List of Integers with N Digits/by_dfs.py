from typing import List

class Solution:
    def printNumbers(self, n: int) -> List[int]:

        def dfs( idx ):

            if idx == n:
                dfs.result.append( int( ''.join( num ) ) )
                return

            for i in range(10):
                num[idx] = str(i)
                dfs(idx+1)

            return


        # -------------------------------

        num = ['0' for _ in range(n) ]
        dfs.result = []
        dfs(idx=0)
        
        # return answer ans skip the first 0
        return dfs.result[1:]


# n : the digit length in decimal

## Time Complexiy: O( 10^n )
#
# The overhead in time is the cost of number enumeration, which is of O( 10^n )

## Space Complexity: O( 10^n )
#
# The overhead in space is the storage for output list, which is of O( 10^n )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().printNumbers( n=1 )
        self.assertEqual( result, [x for x in range(1, 10**1) ] )


    def test_case_2( self ):

        result = Solution().printNumbers( n=2 )
        self.assertEqual( result, [x for x in range(1, 10**2) ] )


if __name__ == '__main__':

    unittest.main()