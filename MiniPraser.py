# leetcode 385. Mini Parser
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """
from collections import deque
class Solution:
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        q = deque()
        n = NestedInteger()
        q.append(n)
        i = 0
        while(i<len(s)):
            if s[i]=='[':
                n = NestedInteger()
                i+=1
                q[-1].add(n)
                q.append(n)
            elif s[i]==']':
                i+=1
                q.pop()
            elif s[i]==',':
                i+=1
            else:
                j = i
                while j<len(s) and s[j] in '1234567890-':
                    j+=1
                q[-1].add(int(s[i:j]))
                i=j
        return q[0].getList()[0]