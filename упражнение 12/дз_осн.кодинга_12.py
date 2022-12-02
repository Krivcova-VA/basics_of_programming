#блок А
#2
from random import randint
x = randint(1,10)
y = randint(1,10)
def F(x,y):
    if x > y:
        return F(x-y,y)
    else:
        return x
print(x,y,F(x,y))
# блок Б
# 1
def F():
    mx = 0
    a = int(input())
    if a == 0:
        return 0
    else:
        mx = max(a,F())
        return mx
print(F())
