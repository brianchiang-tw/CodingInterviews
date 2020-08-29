class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:

        # -----------------------------------------------
        def digits_sum( x ):

            if x < 10:
                return x
            
            else:
                return digits_sum( x // 10 ) + ( x % 10 )

        # -----------------------------------------------
        def dfs( x, y ):

            if x < 0 or x == m or y < 0 or y == n or \
            (x, y) in dfs.visited or                \
            (digits_sum(x) + digits_sum(y)) > k:

                # out-of-boundary
                # visited
                # digits sum > k
                return 
            
            
            dfs.visited.add( (x, y) )
            dfs.counter += 1

            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

        # -----------------------------------------------
        dfs.counter = 0
        dfs.visited = set()
        dfs( x=0, y=0 )

        return dfs.counters



# m : the dimension of height
# n : the dimension of width

## Time Complexity: O( m * n )
#
# The overhead in time is the cost of DFS, which is of O( m * n )

## Space Complexity: O( m * n )
#
# Theo overhead in space is the storage for visited set, which is of O( m * n )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().movingCount( m=2, n=3, k=1 )
        self.assertEqual(result, 3)


    def test_case_2( self ):

        result = Solution().movingCount( m=3, n=1, k=0 )
        self.assertEqual(result, 1)



if __name__ == '__main__':

    unittest.main()
