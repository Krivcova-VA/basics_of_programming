#1
a = int(input())
b = int(input())
for i in range(a,b+1):
    print(i)
#2
a = int(input())
b = int(input())
if a < b:
    for i in range(a,b+1):
        print(i)
else:
    for i in range(a,b-1,-1):
        print(i)
#3
a = int(input())
b = int(input())
if a > b:
    for i in range(a,b-1,-1):
        if i % 2 != 0:
            print(i)
#4
s = 0
n = int(input())
while n > 0:
    a = int(input())
    s += a
    n -= 1
print(s)
#5
n = int(input())
s = 0
for i in range(1,n+1):
    s += i**3
print(s)
#6
f = 1
n = int(input())
for i in range(1,n+1):
    f *= i
print(f)
#7
s = 0
a = 1
n = int(input())
for i in range(1,n+1):
    a *= i
    s += a
print(s)
#8
k = 0
s = ""
while k <= 9:
    k += 1
    s += f"{k}"
    print(s)
#9
k = [0,1]
n = int(input()) - 2
while n > 0:
    k.append(k[-2]+k[-1])
    n -= 1
print(sum(k))
