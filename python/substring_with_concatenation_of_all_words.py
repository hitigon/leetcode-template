# coding=utf-8
# AC Rate: 18.1%
# https://oj.leetcode.com/problems/substring-with-concatenation-of-all-words/

# You are given a string, S, and a list of words, L, that are all of the same
# length. Find all starting indices of substring(s) in S that is a concatenation
# For example, given:
# S: "barfoothefoobarman"
# L: ["foo", "bar"]
# You should return the indices: [0,9].
# (order does not matter).

class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        