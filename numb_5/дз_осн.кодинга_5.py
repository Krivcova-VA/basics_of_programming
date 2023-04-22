#1
n = int(input())
def F(n):
    k = 1
    while k <= n:
        print(k**2)
        k += 1
F(n)
#2
n = int(input())
def F(n):
    d = 2
    if n > 2:
        while n % d != 0:
            d += 1
    print(d)
F(n)
#3
n = int(input())
def F(n):
    cnt = 0#показатель
    a = 1#сама степень
    if n > 0:
        while n // 2 > 0:
            n = n // 2
            cnt += 1
            a *= 2
    print(cnt,a)
F(n)
#4
x = int(input())
y = int(input())
def F(x,y):
    cnt = 0
    while x < y:
        x *= 1.1
        cnt += 1
    print(cnt)
F(x,y)
5
def F():
    n = int(input())
    cnt = 1
    if n > 0:
        while n != 0:
            n = int(input())
            cnt += 1
    print(cnt-1)
F()
#6
def F():
    a = int(input())
    s = a
    cnt = 1
    while a != 0:
        a = int(input())
        cnt += 1
        s += a
    print(s,cnt,s/cnt)
F()
#7
def F():
    cnt = 0
    a = int(input())
    while a <= 0:
        break
    while a > 0:
        b = int(input())
        if a < b:
            cnt += 1
        a = b
    print(cnt)
F()
#8
def F():
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
F()








