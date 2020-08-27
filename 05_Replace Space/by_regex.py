from re import sub, compile
class Solution:
    def replaceSpace(self, s: str) -> str:

        pattern = compile(r'\s')
        return sub(pattern, '%20', s)

# n : the character length of s

## Time Complexity: O( n )
#
# The overhead in time is the cost of iteration on string, which is of O( n )

## Space Comeplxtiy: O( n )
#
# The overhead in space is the storage for string output, which is of O( n ).


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().replaceSpace(s="We are happy.")
        self.assertEqual(result, "We%20are%20happy.")


    def test_case_2( self ):

        result = Solution().replaceSpace(s="How are you?")
        self.assertEqual(result, "How%20are%20you?")



if __name__ == '__main__':

    unittest.main()