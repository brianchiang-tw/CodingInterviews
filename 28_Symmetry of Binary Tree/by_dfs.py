# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        # ------------------------------
        def check_symm(p, q) -> bool:

            if not p and not q:
                return True

            elif p and q:
                return p.val == q.val and check_symm(p.left, q.right) and check_symm(p.right, q.left)
            else:
                return False

        # ------------------------------
        return check_symm(p=root.left, q=root.right) if root else True



# n : the number of nodes in binary tree

## Time Complexity: O( n )
# 
# The overhead in time is the cost of dfs of binary tree, which is of O( n )


## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):
        
        root = TreeNode( 1 )

        root.left = TreeNode( 2 )
        root.right = TreeNode( 2 )

        root.left.left = TreeNode( 3 )
        root.left.right = TreeNode( 4 )
        root.right.left = TreeNode( 4 )
        root.right.right = TreeNode( 3 )

        result = Solution().isSymmetric( root )
        self.assertEqual(result, True)


    def test_case_2( self ):
        
        root = TreeNode( 1 )

        root.left = TreeNode( 2 )
        root.right = TreeNode( 2 )

        root.left.right = TreeNode( 3 )
        root.right.right = TreeNode( 3 )

        result = Solution().isSymmetric( root )
        self.assertEqual(result, False)



if __name__ == '__main__':

    unittest.main()