# leetcode 735. Asteroid Collision
from collections import deque
class Solution:
    def asteroidCollision(asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        # ans time limit exceeded
        # ans = []
        # stack = deque()
        # for i in asteroids:
        #     stack.append(i)
        # i = 0
        # while(i<len(asteroids) and stack):
        #     print(stack)
        #     tmp = deque()
        #     tmp.append(stack[0])
        #     for j in range(1,len(stack)):
        #         if tmp:
        #             a = tmp.pop()
        #         else:
        #             tmp.append(stack[j])
        #             continue
        #         b = stack[j]
        #         print(tmp,a,b)
        #         if b<0 and a>0:
        #             if b+a<0:
        #                 num = b
        #                 tmp.append(num)
        #             elif b+a>0:
        #                 num = a
        #                 tmp.append(num)
        #             else:
        #                 i+=1
        #         else:
        #             tmp.append(a)
        #             tmp.append(b)
        #     stack = tmp
        #     i+=1
        # for i in stack:
        #     ans.append(i)
        # return ans
        stack = []
        for i in asteroids:
            if i>0:
                stack.append(i)
            elif i<0:
                while stack and 0<stack[-1]<-i:
                    stack.pop()
                if stack and 0<stack[-1]:
                    if stack[-1]==-i:
                        stack.pop()
                else:
                    stack.append(i)
        return stack
print(Solution.asteroidCollision([1,-1,1,-1]))


