# #1
# n = int(input())
# k = 1
# while k <= n:
#     print(k**2)
#     k += 1
# #2
# n = int(input())
# d = 2
# if n > 2:
#     while n % d != 0:
#         d += 1
# print(d)
# #3
# n = int(input())
# cnt = 0#показатель
# a = 1#сама степень
# if n > 0:
#     while n // 2 > 0:
#         n = n // 2
#         cnt += 1
#         a *= 2
# print(cnt,a)
# #4
# x = int(input())
# y = int(input())
# cnt = 0
# while x < y:
#     x *= 1.1
#     cnt += 1
# print(cnt)
# #5
# n = int(input())
# cnt = 1
# if n > 0:
#     while n != 0:
#         n = int(input())
#         cnt += 1
# print(cnt-1)
# #6
# a = int(input())
# s = a
# cnt = 1
# while a != 0:
#     a = int(input())
#     cnt += 1
#     s += a
# print(s,cnt,s/cnt)
# #7
# cnt = 0
# a = int(input())
# while a <= 0:
#     break
# while a > 0:
#     b = int(input())
#     if a < b:
#         cnt += 1
#     a = b
# print(cnt)
#8
cnt = 1
max_cnt = 0
a = int(input())
while a <= 0:
    break
while a > 0:
    b = int(input())
    if a == b:
        cnt += 1
        max_cnt = max(max_cnt,cnt)
    else:
        cnt = 1
        a = b
print(max_cnt)









