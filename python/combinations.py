# coding=utf-8
# AC Rate: 30.3%
# SOURCE URL: https://oj.leetcode.com/problems/combinations/
#
#
# Given two integers n and k, return all possible combinations of k numbers out
#  of 1 ... n.
#
#
# For example,
# If n = 4 and k = 2, a solution is:
#
#
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#
#


class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        