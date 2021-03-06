# coding=utf-8
# AC Rate: 20.7%
# https://oj.leetcode.com/problems/insert-interval/

# Given a set of non-overlapping intervals, insert a new interval into the
# You may assume that the intervals were initially sorted according to their
# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as
# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        