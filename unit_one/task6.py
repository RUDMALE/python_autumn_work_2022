#todo: Дана сторона квадрата a. Найти его площадь S = a²
# Примечание: сторону квадрата получаем через функцию input().
# При решении задачи обратите внимание какой тип вы получаете через функцию input().
print("Вычисление площади квадрата")
print("ВВедите сторону квадрата")
a = input ()
print(type(a))
a=int(a)
s=a**2
print("Площадь квадрата =",s)