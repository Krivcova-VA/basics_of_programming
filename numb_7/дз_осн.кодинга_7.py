#вариант14
#1
def F():
    n = int(input())
    lst = [int(input()) for i in range(n)]
    print(lst)
    a = lst.index(max(lst))
    b = lst.index(min(lst))
    lst[a],lst[b] = min(lst),max(lst)
    print(lst)
F()
#2
def F():
    lst = [int(input()) for i in range(10)]
    print(lst)
    sr = sum(lst)/10
    for i in range(len(lst)):
        if lst[i] > sr:
            lst[i] = 1
    print(sr)
    print(lst)
F()
