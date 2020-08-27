# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import List
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        
        stack = [ head ] if head else []

        rev_path = []

        while stack:

            top_node = stack[-1]

            if top_node and top_node.next:
                stack.append( top_node.next )
            
            else:
                break

        while stack:
            rev_path.append( stack.pop().val )
        
        return rev_path


# n : the length of input linked list

## Time Complexity: O( n )
#
# The overhead in time is the cost of linked list traversal, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for stack, which is of O( n )



def linked_list_builder( arr=[] ):

    cur, last = None, None

    for node_value in reversed(arr):

        cur = ListNode(node_value)
        cur.next = last
        last = cur
    
    head_of_linked_list = last
    return head_of_linked_list



def traverse_linked_list( node ):

    path = []

    cur = node
    while cur:
        path.append( cur.val )
        cur = cur.next

    return path


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        head = linked_list_builder(arr=[1,2,3,4,5])
        result = Solution().reversePrint(head)
        self.assertEqual(result, [5,4,3,2,1] )


    def test_case_2( self ):

        head = linked_list_builder(arr=[1,2])
        result = Solution().reversePrint(head)
        self.assertEqual(result, [2,1] )


    def test_case_3( self ):

        head = linked_list_builder(arr=[1])
        result = Solution().reversePrint(head)
        self.assertEqual(result, [1] )


    def test_case_4( self ):

        head = linked_list_builder(arr=[])
        result = Solution().reversePrint(head)
        self.assertEqual(result, [] )


if __name__ == '__main__':

    unittest.main()