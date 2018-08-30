# 找周期
# #coding=utf-8
# import sys
# a = []
# def CalMin(L):
#     min = L[L[0]]
#     max = L[1]
#     for i in range(1,L[0]-1):
#         if min>L[i+1]-L[i]:
#             min = L[i+1]-L[i]
#         if max<L[i+1]-L[i]:
#             max = L[i+1]-L[i]
#     return (min,max)
#
# def CalOneLine(L):
#     Min,Max = CalMin(L)
#     a1 = L[1]
#     an = L[L[0]]
#     for j in range(Min, Max+1, Min):
#         flag = True
#         for t in range(1, L[0]):
#             if L[t] + j <= an and not (L[t]+j in L):
#                 flag = False
#                 break
#             if L[t] - j >= a1 and not (L[t]-j in L):
#                 flag = False
#                 break
#         if flag == True:
#             return j
#
# if __name__ == "__main__":
#     n = int(sys.stdin.readline().strip())
#     for i in range(n):
#         tmp = []
#         line = sys.stdin.readline().strip()
#         values = list(map(int, line.split()))
#         for j in range(0,values[0]+1):
#             tmp.append(values[j])
#         a.append(tmp)
#     for i in range(len(a)):
#         one = CalOneLine(a[i])
#         print(one)
# 在日常书面表达中，我们经常会碰到很长的单词，比如"localization"、"internationalization"等。为了书写方便，
# 我们会将太长的单词进行缩写。这里进行如下定义：

