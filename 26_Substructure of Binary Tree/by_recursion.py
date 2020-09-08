# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:

        def similar(a, b):

            if not b: 
                # b is empty node or empty tree
                return True
            elif (not a) or (a.val != b.val):
                # a is empty tree, or nodes value are different
                return False
            
            return similar(a.left, b.left) and similar(a.right, b.right)

        # ---------------------------------------------------
        return bool( A and B) and ( similar(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B) )



# m : the number of nodes in binary tree A
# n : the number of nodes in binary tree B

## Time Complexity: O( m*n )
#
# The overhead in time is the cost of dfs, with each node as start node in A, which is of O( m*n )

## Space Complexity: O( m )
#
# The overhead in space is the storage for recursion stack, which is of O( m )


import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):

        a = TreeNode( 1 )
        a.left = TreeNode( 2 )
        a.right = TreeNode( 3 )

        b = TreeNode( 3 )
        b.left = TreeNode( 1 )

        result = Solution().isSubStructure(A=a, B=b)
        self.assertEqual(result, False)


    def test_case_2( self ):

        a = TreeNode( 3 )

        a.left = TreeNode( 4 )
        a.right = TreeNode( 5 )

        a.left.left = TreeNode( 1 )
        a.left.right = TreeNode( 2 )

        b = TreeNode( 4 )
        b.left = TreeNode( 1 )

        result = Solution().isSubStructure(A=a, B=b)
        self.assertEqual(result, True)



if __name__ == '__main__':

    unittest.main()        