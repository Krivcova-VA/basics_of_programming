#1
print("Курс Основы программирования начался")
#2
print((16823*12302)%3092)
#3
age = int(input())
name = str(input())
if (age > 0) and (age < 75) and ("Иван" != name):
    if age >= 16:
        print("Поздравляем вы поступили в ВГУИТ",name)
    if age < 16:
        print("Сначала нужно окончить школу!",age)
#4
seconds = int(input())
print(seconds // 86400,seconds//360,seconds//60,seconds)
#5
n = int(input())
print(n + n**2 + n**3 + n**4 + n**5)
#6
x = 1
y = 0
y_1 = y 
y = x
x = y_1
print(x,y)
#7
number = int(input())
if number % 2 == 0:
    print(1)
else:
    print(0)