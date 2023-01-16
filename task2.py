# Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.
data = open('frut.txt', encoding='utf-8')
fruts = data.readlines()
data.close()
print(fruts)
frut = []
letter = input('Введите букву: ')

res = [idx for idx in fruts if idx[0].lower() == letter.lower()]
print(res)


