# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        val_idx_dict = { val: idx for idx, val in enumerate(inorder) }
        
        self.head_index = 0

        # ----------------------------------------------

        def helper(left, right):
            
            if left <= right:
                # base case:
                # rebuild binary tree with definition of preorder traversal
                # (Center, Left subtree, Right subtree)
                root_val = preorder[self.head_index]
                self.head_index += 1

                root = TreeNode( root_val )
                root_idx = val_idx_dict[root_val]

                root.left = helper(left, root_idx-1)
                root.right = helper(root_idx+1, right)
                return root

            else:
                # base case:
                # leaf node, return None as dummy
                return None

        # ----------------------------------------------

        return helper(left=0, right=len(inorder)-1)



# n : the length of input list, inorder

## Time Complexity: O( n )
#
# The overhead in the cost of rebuilding of preorder traversal, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n )


def inorder_path( node ):

    if node:

        yield from inorder_path( node.left )
        yield node.val
        yield from inorder_path( node.right )



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().buildTree( preorder = [3,9,20,15,7], inorder = [9,3,15,20,7] )
        inorder_traversal = [ *inorder_path(result) ]

        self.assertEqual( inorder_traversal, [9,3,15,20,7] )



if __name__ == '__main__':

    unittest.main()
