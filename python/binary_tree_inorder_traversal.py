# coding=utf-8
# AC Rate: 35.6%
# https://oj.leetcode.com/problems/binary-tree-inorder-traversal/

# Given a binary tree, return the inorder traversal of its nodes' values.
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].
# Note: Recursive solution is trivial, could you do it iteratively?
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized
# OJ's Binary Tree Serialization:
# The serialization of a binary tree follows a level order traversal, where '#'
# Here's an example:
#    1
#   / \
#  2   3
#     /
#    4
#     \
#      5
# The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        