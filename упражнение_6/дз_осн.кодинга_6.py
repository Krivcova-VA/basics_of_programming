#вариант14
s = str(input())
s = s.split(" ")
for i in s:
    if i[0] == "а" or i[-1] == "я":
        print(i)