# coding=utf-8
# AC Rate: 16.5%
# https://oj.leetcode.com/problems/word-break-ii/

# Given a string s and a dictionary of words dict, add spaces in s to construct a
# Return all such possible sentences.
# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].
# A solution is ["cats and dog", "cat sand dog"].

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        