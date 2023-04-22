#вриант14
#1
def F():
    with open('C:/Users/vkriv/учеба/осн.кодинга/задание_10/file.txt', 'r') as f:
            a1 = [[int(num) for num in line.split(',')] for line in f]
    a = [list(i) for i in zip(*a1)]
    m = int(input())
    max_elem = 0
    for i in a:
        print(i)
        for j in range(len(a)):
            if max_elem < int(a[i][j]):
                m1 = i
    a[m1], a[m] = a[m],a[m1]
    print(a)

    with open('C:/Users/vkriv/учеба/осн.кодинга/задание_10/file.txt', 'w') as file:
        print(*a, file=file, sep=",\n", end="\n")
F()
#2
#n - размерность матрицы n x n
#mat - результирующая матрица
#st - текущее значение-счетчик для записи в матрицу
#m - коеффициент, используемый для заполнения верхней матрицы последующих
# витков, т.к. одномерные матрицы следующих витков имеют меньше значений
n = int(input())
def F(n):
    mat = [[0]*n for i in range(n)]
    st, m = 1, 0
    # Заранее присваиваю значение центральному элементу матрицы
    mat[n//2][n//2]=n*n
    for v in range(n//2):
        #Заполнение верхней горизонтальной матрицы
        for i in range(n-m):
            mat[v][i+v] = st
            st+=1
            #i+=1
        #Заполнение правой вертикальной матрицы    
        for i in range(v+1, n-v):
            mat[i][-v-1] = st
            st+=1
            #i+=1
        #Заполнение нижней горизонтальной матрицы
        for i in range(v+1, n-v):
            mat[-v-1][-i-1] =st
            st+=1
            #i+=1
        #Заполнение левой вертикальной матрицы
        for i in range(v+1, n-(v+1)):
            mat[-i-1][v]=st
            st+=1
            #i+=1
        #v+=1
        m+=2
    #Вывод результата на экран
    for i in mat:
        print(*i)
F(n)   

