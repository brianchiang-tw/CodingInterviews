# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:

        if root:
            # general case
            root.left, root.right = root.right, root.left

            self.mirrorTree( root.left )
            self.mirrorTree( root.right )

            return root

        else:
            # base case aka stop condition
            return None



# n : the number of node in binary tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for recurison call stack, which is of O( n )



def inorder( node ):

    if node:

        yield from inorder( node.left )
        yield node.val
        yield from inorder( node.right )


import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):

        root = TreeNode( 4 )

        root.left = TreeNode( 2 )
        root.right = TreeNode( 7 )

        root.left.left = TreeNode( 1 )
        root.left.right = TreeNode( 3 )
        root.right.left = TreeNode( 6 )
        root.right.right = TreeNode( 9 )

        Solution().mirrorTree(root=root)

        inorder_path = [ *inorder(root) ]
        self.assertEqual(inorder_path, [9,7,6,4,3,2,1])



if __name__ == '__main__':

    unittest.main()