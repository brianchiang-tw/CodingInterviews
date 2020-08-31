# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # ----------------------------------------
        def helper(prev, node):

            if node and node.next:

                _next = helper(node, node.next)
                _next.next = node
                node.next = prev

                return node
            
            else:

                helper.new_head = node
                return node

        # ----------------------------------------
        helper(prev=None, node=head)
        return helper.new_head



# n : the length of linked list

## Time Complexity: O( n )
#
# The overhead in time is the cost of recursion, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n )



def gen_linked_list( arr ):

    cur, last = None, None

    for number in reversed(arr):

        cur = ListNode(number)
        cur.next = last
        last = cur

    return last


def visit_linked_list( head ):

    cur = head

    while cur:
        
        
        yield cur.val
        cur = cur.next



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        head = gen_linked_list(arr=[1,2,3,4,5])
        new_head = Solution().reverseList(head=head)
        result = [ *visit_linked_list(head=new_head) ]

        self.assertEqual(result, [5,4,3,2,1])


    def test_case_2( self ):

        head = gen_linked_list(arr=[1,2])
        new_head = Solution().reverseList(head=head)
        result = [ *visit_linked_list(head=new_head) ]

        self.assertEqual(result, [2,1])


    def test_case_3( self ):

        head = gen_linked_list(arr=[1])
        new_head = Solution().reverseList(head=head)
        result = [ *visit_linked_list(head=new_head) ]

        self.assertEqual(result, [1])


    def test_case_4( self ):

        head = gen_linked_list(arr=[])
        new_head = Solution().reverseList(head=head)
        result = [ *visit_linked_list(head=new_head) ]

        self.assertEqual(result, [])


if __name__ == '__main__':

    unittest.main()