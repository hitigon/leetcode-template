# coding=utf-8
# AC Rate: 21.2%
# https://oj.leetcode.com/problems/word-break/

# Given a string s and a dictionary of words dict, determine if s can be
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
# Return true because "leetcode" can be segmented as "leet code".

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        