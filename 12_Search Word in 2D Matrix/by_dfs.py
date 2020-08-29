from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        h, w = len(board), len(board[0])

        def dfs(x, y, index):


            

            if x < 0 or x >= w or y < 0 or y >= h or board[y][x] != word[index]:
                
                # Reject 
                # if current position is out of boundary or it does not match the character of word
                
                return False

            if index == len(word) - 1:

                # Accept:
                # match all characters
                return True




            cur = board[y][x]

            # mark as '#' to avoid repeated travesal
            board[y][x] = '#'

            found = dfs(x, y+1, index+1) or dfs(x, y-1, index+1) or dfs(x+1, y, index+1) or dfs(x-1, y, index+1)

            # restore original status
            board[y][x] = cur

            return found

        # ----------------------------------------------
        return any( dfs(x, y, index=0) for y in range(h) for x in range(w) )


# m : the dimension of board height
# n : the dimension of board width
# s : the character length of input string

## Time Comeplxtiy: O( m * n * (s^4) )
#
# The overhead in time is the cost of dfs on each board grid.

## Space Complexity: O( s^4 )
#
# The overhead in space is  the storage for recursion call stack.



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):
        board = [
                    ["A","B","C","E"],
                    ["S","F","C","S"],
                    ["A","D","E","E"],
                ]

        word = "ABCCED"
        result = Solution().exist( board, word)
        self.assertEqual( result, True)


    def test_case_2( self ):

        board = [
                    ["a","b"],
                    ["c","d"],
                ]

        word = "abcd"
        result = Solution().exist( board, word)
        self.assertEqual( result, False)

    
    def test_case_3( self ):

        board = [
                    ["a","b"],
                    ["c","d"],
                ]

        word = "abdc"
        result = Solution().exist( board, word)
        self.assertEqual( result, True)


if __name__ == '__main__':

    unittest.main()