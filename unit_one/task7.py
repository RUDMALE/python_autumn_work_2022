#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().
# При решении задачи обратите внимание какой тип вы получаете через функцию input().

print("Вычисление длины отрезков AC и BC и их сумму")
print("ВВедите три точки A , B , C на числовой оси")
print("Введите точку А =")
a = input ()
print(type(a))
a=int(a)
print("Введите точку B =")
b = input ()
print(type(b))
b=int(b)
print("Введите точку C =")
c = input ()
print(type(c))
c=int(c)
ab = b-a
print("Длина отрезка АВ=", ab)
bc = c-b
print("Длина отрезка BC=", bc)
ac = ab+bc
print("Сумма отрезков =", ac)