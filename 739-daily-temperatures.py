"""
Problem Link: https://leetcode.com/problems/daily-temperatures/

Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have 
to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(T)
        stack = [] #indexes from hottest to coldest
        for i in xrange(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans