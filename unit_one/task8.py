#todo: Даны переменные A, B, C. Написать код который меняет местами переменные таким образом
# чтобы значения в переменных были расположены по возрастанию
# Пример 1:
A = 10
B = 3
C = 7
# Итоговый результат должен быть:
# A = 3
# B = 7
# C = 10

# Пример 2:
A = 2
B = 10
C = 7
# Итоговый результат должен быть:
# A = 2
# B = 7
# C = 10

print("ВВедите три значения A , B , C ")
a=int(input("Введите  А ="))
b=int(input("Введите  B ="))
c=int(input("Введите  с ="))
print("Вы ввели следующие данные:")
print("A=",a)
print("B=",b)
print("C=",c)
print("Перестановка по возрастанию")
if a >=b:
    if a >= c:
        c_n=a
        if b>=c:
            b_n=b
            a_n=c
            print("А=",a_n)
            print("B=",b_n)
            print("C=",c_n)
        else:
            b_n=c
            a_n=b
            print("А=", a_n)
            print("B=", b_n)
            print("С=", a_n)
    else:
        c_n=c
        b_n=a
        a_n=b
        print("А=", a_n)
        print("B=", b_n)
        print("С=", c_n)
else:
    if b>=c:
        c_n=b
        b_n=c
        a_n=a
        print("А=", a_n)
        print("B=", b_n)
        print("С=", c_n)
    else:
        c_n=c
        b_n=b
        a_n=a
        print("А=", a_n)
        print("B=", b_n)
        print("С=", c_n)







