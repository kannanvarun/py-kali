# https://leetcode.com/problems/group-anagrams/
# Group anagrams -
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
from collections import defaultdict
from typing import List


class Solution:
    # using python dict
    # def groupAnagram(self, strs: List[str]) -> List[List[str]]:
    #     if strs == [""]:
    #         return [[""]]
    #     d = dict()
    #     for _s in strs:
    #         _s1 = "".join(sorted(_s))
    #         if _s1 in d.keys():
    #             d[_s1].append(_s)
    #         else:
    #             d[_s1] = [_s]
    #     _sol = [_v for _v in d.values()]
    #     return _sol

    # using collections defaultdict
    def groupAnagram(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for _s in strs:
            d["".join(sorted(_s))].append(_s)
        return d.values()


s = ["eat","tea","tan","ate","nat","bat"]
# s = [""]
# s = ["a"]
g = Solution()
soln = g.groupAnagram(s)
print(soln)