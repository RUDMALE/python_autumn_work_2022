#todo: Выведите все строки данного файла в обратном порядке.
# Для этого считайте список всех строк при помощи метода readlines().
#Содержимое файла import_this.txt
#Beautiful is better than ugly.
#Explicit is better than implicit.
#Simple is better than complex.
#Complex is better than complicated.

#выходные данные
#Complex is better than complicated.
#Simple is better than complex.
#Explicit is better than implicit.
#Beautiful is better than ugly.

#FILE = "import_this.txt"
f = open("import_this.txt", "rt")

lines = f.readlines()
lines.reverse()
lines = [line.rstrip() for line in lines]
print("\n".join(lines))

f.close()