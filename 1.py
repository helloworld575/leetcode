# #coding=utf-8
# import sys
# a = sys.stdin.readline().strip()
# b = sys.stdin.readline().strip()
# a = list(map(int, a.split()))
# b = list(map(int, b.split()))
# sum = []
# for i in range(int(a[0])):
#     for j in range(int(a[0])):
#         if int(b[i])-int(b[j])==a[1]:
#             if b[i]>b[j]:
#                 sum.append([b[i],b[j]])
#             else:
#                 sum.append([b[j],b[i]])
# ans = len(sum)
# for i in range(len(sum)):
#     x = sum[i][0]
#     y = sum[i][1]
#     if x!=-1 and y!=-1:
#         for j in range(i+1,len(sum)):
#             if x == sum[j][0] and y == sum[j][1]:
#                 ans-=1
#                 sum[j][0]=sum[j][1]=-1
# print(ans)

# # coding=utf-8
# import sys
# line = sys.stdin.readline().strip()
# values = list(map(int, line.split()))
# k = values[0]
# s = 1
# m = 1
# def h(sta, ans, m, s):
#     if s == k:
#         return ans
#     if s + s <= k:
#         if sta == 3 or sta == 4:
#             return h(2, ans + 1, m, s + m)
#         else:
#             return h(1, ans + 1, s, s + s)
#     if s + s > k:
#         if s + m <= k:
#             return h(2, ans + 1, m, s + m)
#         if s + m > k:
#             if sta == 1:
#                 return h(3, ans - 1, s / 4, s / 2)
#             if sta == 2:
#                 return h(4, ans - 1, m, 2 * s / 3)
#
# print(h(0, 0, m, s))

f = open("hello.c", 'r')
text = ""
change = False
fileInAnno = False
file = f.read()
for i in range(len(file)):
    c = file[i]
    if i+1<len(file) and c == '/' and file[i+1]=='*':
        fileInAnno = True
    elif i+1<len(file) and c == '*' and file[i+1]=='/':
        fileInAnno = False
        change = True
        continue
    if fileInAnno == False:
        if change==True:
            change = False
            continue
        text = text+c
print(text)

