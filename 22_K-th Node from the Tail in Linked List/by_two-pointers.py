# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:

        slow, fast = head, head

        while k > 0:
            # fast go with k steps ahead of slow
            fast = fast.next
            k -= 1
        
        while fast:
            # When fast reach None, slow is on the k-th node from the tail
            slow, fast = slow.next, fast.next

        return slow



# n : the length of linked list, which is of O( n ).

## Time Complexity: O( n )
#
# The overhead in time is the cost of while-loop, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for two-pointers, which is of O( 1 )


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
        result = Solution().getKthFromEnd(head, k=2)
        self.assertEqual( [*visit_linked_list(result)], [4,5])


    def test_case_2( self ):

        head = gen_linked_list(arr=[1,2,3,4,5])
        result = Solution().getKthFromEnd(head, k=1)
        self.assertEqual( [*visit_linked_list(result)], [5])


    def test_case_3( self ):

        head = gen_linked_list(arr=[1,2,3,4,5])
        result = Solution().getKthFromEnd(head, k=4)
        self.assertEqual( [*visit_linked_list(result)], [2,3,4,5])        


    def test_case_4( self ):

        head = gen_linked_list(arr=[1,2,3,4,5])
        result = Solution().getKthFromEnd(head, k=5)
        self.assertEqual( [*visit_linked_list(result)], [1,2,3,4,5]) 


if __name__ == '__main__':

    unittest.main()