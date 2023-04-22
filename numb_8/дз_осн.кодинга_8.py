# #вариант14
# #1
# def F():
#     def dell(x):
#         cnt = 0
#         for i in range(1,x+1):
#             if x % i == 0:
#                 cnt += 1
#         return cnt

#     m = int(input())
#     n = int(input())
#     deliteli = []
#     deliteli = [dell(i) for i in range(m,n+1)]
#     for i in range(m,n+1):
#         if dell(i) == max(deliteli):
#             print(i,max(deliteli))
# F()
#2
def F():
    import math
    def dist(m,n): #m,n списки с координатами точек
        return math.sqrt((m[0]-n[0])**2 + (m[1]-n[1])**2)

    x = [int(input()) for i in range(2)]
    print(x)
    y = [int(input()) for i in range(2)]
    print(y)
    z = [int(input()) for i in range(2)]
    print(z)
    p = [int(input()) for i in range(2)]
    print(p)
    print(max(dist(x,y),dist(x,z),dist(x,p),dist(y,z),dist(y,p),dist(z,p)))
F()