#1
a = int(input())
b = int(input())
c = int(input())
print(a+b+c)
#2
a = int(input())
b = int(input())
print(1/2*b*a)
#3
def F(n):
    if n % 60 == 0:
        a = n // 60
        while a > 23:
            a -= 24
        return str(a) + ":00"
    else:
        a = n // 60
        while a > 23:
            a -= 24
        b = n % 60
        if b < 10:
            return str(a) + ":0" +str(b)
        else:
            return str(a) + ":" + str(b)
print(F(156780))
#4
def F(a,b,l,n):
    return n*(a+b)+l+a
print(F(2,3,15,8))
#5
def F(a,b,c):
    return max(max(a,b),c)
print(F(2,23,45))
#6
def F(x1,y1,x2,y2):
    if (((x1 % 2 != 0 and y1 % 2 != 0) or (x1 % 2 == 0 and y1 % 2 == 0)) and
    ((x2 % 2 != 0 and y2 % 2 != 0) or (x2 % 2 == 0 and y2 % 2 == 0))):
        return "Да"
    elif (((x1 % 2 == 0 and y1 % 2 != 0) or (x1 % 2 != 0 and y1 % 2 == 0)) and
    ((x2 % 2 == 0 and y2 % 2 != 0) or (x2 % 2 != 0 and y2 % 2 == 0))):
        return "Да"
    else:
        return "Нет"
print(F(2,4,3,4))
print(F(6,8,5,3))
#7
def F(a):
    if a % 4 == 0:
        if a % 100 != 0:
            return "Да"
        elif a % 4 == 0:
            return "Да"
    else:
        return "Нет"
print(F(2002))
print(F(1988))
#8
def F(x,y,z):
    if x == y:
        if x == z:
            return 3
        else:
            return 2
    else:
        return 0
print(F(22,5,68))
print(F(3,3,5))
print(F(44,44,44))
#9
def F(n,m,k):
    for i in range(m,0,-1):
        if n * i == k:
            return "Да"
        else:
            continue
    else:
        for i in range(n,0,-1):
            if m * i == k:
                return "Да"
            else:
                continue
    return "Нет"
print(F(4,5,11))
print(F(3,4,9))

    
