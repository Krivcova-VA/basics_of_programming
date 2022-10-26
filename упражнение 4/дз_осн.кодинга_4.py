#1
a = int(input())
b = int(input())
def F(a,b):
    if a < b:
        for i in range(a,b+1):
            print(i)
F(a,b)
#2
a = int(input())
b = int(input())
def F(a,b):
    if a < b:
        for i in range(a,b+1):
            print(i)
    else:
        for i in range(a,b-1,-1):
            print(i)
F(a,b)
#3
a = int(input())
b = int(input())
def F(a,b):
    if a > b:
        for i in range(a,b-1,-1):
            if i % 2 != 0:
                print(i)
F(a,b)
#4
n = int(input())
def F(n):
    s = 0
    while n > 0:
        a = int(input())
        s += a
        n -= 1
    print(s)
F(n)
#5
n = int(input())
def F(n):
    s = 0
    for i in range(1,n+1):
        s += i**3
    print(s)
F(n)
#6
n = int(input())
def F(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    print(f)
F(n)
#7
n = int(input())
def F(n):
    s = 0
    a = 1
    for i in range(1,n+1):
        a *= i
        s += a
    print(s)
F(n)
#8
n = int(input())
def F(n):
    k = 0
    s = ""
    if n <= 9:
        while k < n:
            k += 1
            s += f"{k}"
            print(s)
F(n)
#9
n = int(input()) - 2
def F(n):
    k = [0,1]
    while n > 0:
        k.append(k[-2]+k[-1])
        n -= 1
    print(sum(k))
F(n)
#10
n = int(input())
k = int(input())
def F(n):
    a = [0,1]
    for i in range(k+n-2):
        a.append(a[-2]+a[-1])
    print(sum(a[k-1:]))
F(n)