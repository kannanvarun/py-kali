# https://leetcode.com/problems/valid-anagram/
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# solution using recursive function: code for finding string permutations taken from here -
# https://stackoverflow.com/a/20955291

# using string combination & recursive function
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         _temp_str_perm = self.get_str_perm(s)
#         _s_perms = list()
#         [_s_perms.append(_t[0]) for _t in _temp_str_perm]
#         return True if t in _s_perms else False
#
#     def get_str_perm(self, string):
#         string = list(string)
#         n = len(string)
#
#         # Base conditions
#         # If length is 0 or 1, there is only 1 permutation
#         if n in [0, 1]:
#             return [string]
#
#         # If length is 2, then there are only two permutations
#         # Example: [1,2] and [2,1]
#         # if n == 2:
#         # return [string, string[::-1]]
#
#         res = []
#         # For every number in array, choose 1 number and permute the remaining
#         # by calling permute recursively
#         for i in range(n):
#             permutations = self.get_str_perm(string[:i] + string[i+1:])
#             for p in permutations:
#                 res.append([''.join(str(n) for n in [string[i]] + p)])
#
#         return res

# sort both strings, convert to lower case and check if they are equal... thanks Sanjay!
class Solution:
    def __init__(self):
        self.flag = False

    def isAnagram(self, s: str, t: str) -> bool:
        return True if sorted(s, key=str.lower) == sorted(t, key=str.lower) else False


s = Solution()
# _r = s.isAnagram(s="ab", t="ba")
# print("output:", _r)
_r = s.isAnagram(s="act", t="bat")
print("output:", _r)
# _r = s.isAnagram(s="act", t="cta")
# print("output:", _r)

