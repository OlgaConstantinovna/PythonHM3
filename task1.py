#  Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8
data = open('fibonachi.txt',encoding='utf-8')
fib = data.readlines()
data.close()

user_number = int(input('Введите число: '))

print(fib[: user_number])