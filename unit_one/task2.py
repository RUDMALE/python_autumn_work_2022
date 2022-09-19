# Преобразуйте переменную age и foo в число
age = "23"
foo = "23abc"
age=int(age)
# foo=int(foo) !!!я не знаю как отделить число от букв.!!!
print("Преобразуйте переменную age=23 и foo=23abc в число",age)
print(type(age))
# Преобразуйте переменную age в Boolean
age = "123abc"
age=bool(age)
print("Преобразуйте переменную age=123abc в Boolean=",age)
print(type(age))
# Преобразуйте переменную flag в Boolean
flag = 1
flag=bool(flag)
print("реобразуйте переменную flag=1 в Boolean=",flag)
print(type(flag))
# Преобразуйте значение  в Boolean
str_one = "Privet"
str_two = ""
str_one=bool(str_one)
str_two=bool(str_two)
print("Преобразуйте значение  в Boolean",str_one,str_two)
# Преобразуйте значение 0 и 1  в Boolean
x=0
y=1
x=bool(x)
y=bool(y)
print("Преобразуйте значение 0 и 1  в Boolean",x,y)
