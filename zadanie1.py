#1
print('Курс Основы программирования начался')

#2
print((16823*12302)%3092)

#3
name=str(input('Укажите свое имя:'))
if name == ('Иван'):
    print('Вы не тот кто нам нужен')

age=int(input('Укажите свой возраст:'))
if age >= 16 and age < 75:
    print('Поздравляем, вы поступили в ВГУИТ')

elif age < 16 and age > 0:
    print('Сначала нужно окончить школу!')

if age < 16:
    print('Вам осталось учиться в школе:',16-age )
#4
seconds = int(input('Колличество секунд'))
days = seconds // 86400
hours = (seconds % 86400) // 3600
minutes = (seconds % 3600) // 60
sec = seconds % 60
print(days, hours, minutes, sec)
#5
n=int(input('Введите число:'))
answer = n + n**2 + n**3 + n**4 + n**5
print(answer)
#6
x=int(input('Введите значение a'))
y=int(input('Введите значение b'))
z=x
x=y
y=z
print('a=',a)
print('b=',b)
#7
number=int(input('Введите number:'))
if number%2 == 0:
    print ('Четное число')
else:
    print('Нечетное число')