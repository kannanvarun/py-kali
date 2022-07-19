from typing import List

# https://leetcode.com/problems/contains-duplicate/#
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
_in_nums = [[1,2,3,1], [1,2,3,4], [1,1,1,3,3,4,3,2,4,2]]


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # using python list count function
        # for _num in nums:
        # if nums.count(_num) >= 2:
        # return True
        # return False

        # using set
        # _set1 = set()
        # for _num in nums:
        #     if _num in _set1:
        #         return True
        #     _set1.add(_num)
        # return False

        # without built-in functions
        _d = {}
        for _num in nums:
            if _num in _d: return True
            else: _d[_num] = 1
        return False


_sol = Solution()
# input data
for _nums in _in_nums:
    _out = _sol.containsDuplicate(nums=_nums)
    print("output:", _out)