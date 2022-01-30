# 1.Напишите программу, которая найдет все такие числа, которые делятся на 7, но не делятся на 5, от 2000 до 3200 (включая оба). Полученные числа должны быть напечатаны в последовательности, разделенной запятыми, в одной строке.
l1=[]
for i in range(2000, 3201):
    if i%7==0 and i%5!=0:
        l1.append(str(i))

print('Задание 1:')
print(' Список чисел:', l1)
print(' Общее количество: ', len(l1))

# 2. Напишите программу, которая может вычислить факториалы заданных чисел. Результаты должны быть напечатаны в последовательности, разделенной запятыми, в одной строке.

from math import factorial
l2 = [3, 5, 4, -10, 6, 12]
for i in range(len(l2)):
  if l2[i] <= 0:
    print('Задание 2. Внимание, число должно быть положительным:', i)

print("Задание 2. Факториалы заданных чисел:", factorial(l2[i]))

# 3. Напишите программу, которая принимает 2 числа X, Y в качестве входных данных с клавиатуры и генерирует двумерный массив. Значение элемента в i-й строке и j-м столбце массива должно быть i*j.  (нумерация с нуля)

def matrix1(x, y):
    matrix = [[0 for j in range(y)] for i in range(x)]
    for i in range(x):
        for j in range(y):
            matrix[i][j] = i * j
    print('Матрица:', *matrix, sep='\n')
print('Задание 3:')
print('Введите кол-во строк матрицы:')
x = int(input())
print('Введите кол-во столбцов матрицы:')
y = int(input())
matrix1(x, y)

# Веб-сайт требует, чтобы пользователи вводили имя пользователя и пароль для регистрации.
# Напишите программу для проверки правильности ввода пароля пользователями.

import re
def pass1():
  print('Введите пароль:')
  password = input()
  if len(password) < 6:
    print('Некорректный ввод пароля! Пароль должен состоять из более чем 6 символов!')
  elif len(password) > 12:
    print('Некорректный ввод пароля! Пароль должен состоять из менее чем 12 символов!')
  elif not re.search("[$#@]", password):
    print('Некорректный ввод пароля! Пароль должен содержать один из знаков $#@!')
  elif not re.search("[A–Z]", password):
    print('Некорректный ввод пароля! Пароль должен содержать хотя-бы одну заглавную букву!')
  elif not re.search("[0-9]", password):
    print('Некорректный ввод пароля! Пароль должен содержать хотя-бы одино число!')
  elif not re.search("[a-z]", password):
    print('Некорректный ввод пароля! Пароль должен содержать хотя-бы одну строчную букву!')
  else:
    print('Пароль принят!')


pass1()