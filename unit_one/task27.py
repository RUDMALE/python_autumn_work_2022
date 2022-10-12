# todo: Реализовать логику игры "Морской бой". Задано игровое поле 5 на 5 в виде двухмерного массива(список списков).
#  Значением 1 (единицей) обозначают однопалубный корабль в координатах i-ой строки и j-го столбца.
#  Написать игровую логику которая по вводу пары i,j  проверяет попадание и его фиксирует.
#  Для генерации случайных значений 0 и 1 в массиве использовать lambda выражение. Кол-во кораблей может быть случайное
#  в зависимости от генерации. Кол-во попыток пока не ограничивать.

# Пример:

# нужно заменить статическую инициализацию списка на динамическую с помощью lambda выражения.
# row_one   = [0, 0, 0, 1, 0]
# row_two   = [0, 0, 0, 1, 0]
# row_three = [0, 1, 0, 0, 0]
# row_four  = [0, 0, 0, 1, 0]
# row_five  = [0, 0, 0, 1, 0]
#
# game_field.append(row_one)
# game_field.append(row_two)
# game_field.append(row_three)
# game_field.append(row_four)
# game_field.append(row_five)
# i = 0  # вхождение в первый массив
# j = 3  # вхождение в 4-ый элемент текущего массива
# # доступ к элементам двухмерного массива
# print(game_field[i][j])

game_field = []  # поле где ставяться корабли
game_field_p = []  # поле где будет видно куда стреляли
max_count = 25  # максимальное количество попыток
count = 0       # начальное количество попыток
print ("Игра Морской бой.")
print ("поле 5 на 5" )
row_one_p   = ["?", "?", "?", "?", "?"]
row_two_p   = ["?", "?", "?", "?", "?"]
row_three_p = ["?", "?", "?", "?", "?"]
row_four_p  = ["?", "?", "?", "?", "?"]
row_five_p  = ["?", "?", "?", "?", "?"]
game_field_p.append(row_one_p)
game_field_p.append(row_two_p)
game_field_p.append(row_three_p)
game_field_p.append(row_four_p)
game_field_p.append(row_five_p)

import random
row_one = [(lambda i : random.randint(0,1))(i) for i in range (0,5)]
row_two = [(lambda i : random.randint(0,1))(i) for i in range (0,5)]
row_three = [(lambda i : random.randint(0,1))(i) for i in range (0,5)]
row_four = [(lambda i : random.randint(0,1))(i) for i in range (0,5)]
row_five = [(lambda i : random.randint(0,1))(i) for i in range (0,5)]
# print (row_one)
# print (row_two)
# print (row_three)
# print (row_four)
# print (row_five)
game_field.append(row_one)
game_field.append(row_two)
game_field.append(row_three)
game_field.append(row_four)
game_field.append(row_five)
# Начало игры
while count < max_count:
    i = int(input("выбирите строчку от 0 до 4   =>"))  # вхождение в первый массив
    j = int(input("выбирите столбец от 0 до 4   =>"))  # вхождение в 4-ый элемент текущего массива
#print(game_field[i][j])
    f = game_field[i][j]
    if f == 1:
      print("УРА! Вы попали в корабль")
      game_field_p[i][j] = 1
      count += 1
      for a in game_field_p:
          print(*a)
    else:
         print("Пробуем еще раз")
         game_field_p[i][j] = 0
         for a in game_field_p:
             print(*a)
         count += 1



