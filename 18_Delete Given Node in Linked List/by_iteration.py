# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:

        dummy_head = ListNode(float('inf'))
        dummy_head.next = head

        prev, cur = dummy_head, head

        while cur:

            if cur.val == val:
                prev.next = cur.next
                break

            else:
                prev, cur = cur, cur.next

        return dummy_head.next



# n : the length of linked list

## Time Complexity: O( n )
#
# The overhead in time is the cost to locate target node in linked list, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for temproary varible and loop index, which is of O( 1 )



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

        head = gen_linked_list( arr=[4,5,1,9] )
        head = Solution().deleteNode(head=head, val=5)
        self.assertEqual( list(visit_linked_list(head)), [4,1,9] )


    def test_case_2( self ):

        head = gen_linked_list( arr=[4,5,1,9] )
        head = Solution().deleteNode(head=head, val=1)
        self.assertEqual( list(visit_linked_list(head)), [4,5,9] )


    def test_case_3( self ):

        head = gen_linked_list( arr=[4,5,1,9] )
        head = Solution().deleteNode(head=head, val=4)
        self.assertEqual( list(visit_linked_list(head)), [5,1,9] )


    def test_case_4( self ):

        head = gen_linked_list( arr=[4,5,1,9] )
        head = Solution().deleteNode(head=head, val=9)
        self.assertEqual( list(visit_linked_list(head)), [4,5,1] )


if __name__ == '__main__':

    unittest.main()
        