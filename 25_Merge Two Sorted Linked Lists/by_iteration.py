# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummy_head = ListNode('#')
        cur = dummy_head

        while l1 and l2:

            if l1.val < l2.val:
                cur.next = l1
                cur, l1 = cur.next, l1.next

            else:
                cur.next = l2
                cur, l2 = cur.next, l2.next
        
        if l2:
            cur.next = l2
        
        elif l1:
            cur.next = l1
        
        return dummy_head.next


# m : the length of first linked list
# n : the length of seconf linked list

## Time Complexity: O( m + n )
#
# The overhead in time is the cost of recursion, which is of O( m + n )

## Space Complexity: O( m + n )
#
# The overhead in space is the storage for recursion call stack, which is of O( m + n )


import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):
        l1 = gen_linked_list(arr=[1,3,5])
        l2 = gen_linked_list(arr=[2,4,6])
        m = Solution().mergeTwoLists(l1, l2)
        result = [ *visit_linked_list(m) ]

        self.assertEqual(result, [1,2,3,4,5,6])

    
    def test_case_2( self ):
        l1 = gen_linked_list(arr=[1,3,5])
        l2 = gen_linked_list(arr=[2,3,4])
        m = Solution().mergeTwoLists(l1, l2)
        result = [ *visit_linked_list(m) ]

        self.assertEqual(result, [1,2,3,3,4,5])



    def test_case_3( self ):
        l1 = gen_linked_list(arr=[1,3,5])
        l2 = gen_linked_list(arr=[])
        m = Solution().mergeTwoLists(l1, l2)
        result = [ *visit_linked_list(m) ]

        self.assertEqual(result, [1,3,5])


    def test_case_4( self ):
        l1 = gen_linked_list(arr=[])
        l2 = gen_linked_list(arr=[1,3,5])
        m = Solution().mergeTwoLists(l1, l2)
        result = [ *visit_linked_list(m) ]

        self.assertEqual(result, [1,3,5])


    def test_case_5( self ):
        l1 = gen_linked_list(arr=[])
        l2 = gen_linked_list(arr=[])
        m = Solution().mergeTwoLists(l1, l2)
        result = [ *visit_linked_list(m) ]

        self.assertEqual(result, [])


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




if __name__ == '__main__':

    unittest.main()