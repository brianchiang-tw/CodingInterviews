class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        seen_zero = False

        for number in nums:
            
            if number:
                # handle for non-zero number

                number = abs(number)

                if nums[number] < 0:
                    # number is repeated
                    return number

                # sign flip at idx
                nums[number] = -nums[number]

            else:
                # handle for zero
                
                if seen_zero:
                    # 0 is repeated
                    return 0
                
                # raise flag for 0's appearance
                seen_zero = True


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().findRepeatNumber(nums=[2, 3, 1, 0, 2, 5, 3])
        self.assertEqual(result in (2,3), True)


if __name__ == '__main__':

    unittest.main()