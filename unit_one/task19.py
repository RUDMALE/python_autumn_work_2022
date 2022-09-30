#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
#– id - номер по порядку (от 1 до 10);
#– текст из списка algoritm
#algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
#"EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]
#Каждое значение из списка должно находится на отдельной строке.

FILE = "algoritm.csv"

algoritm = ["C4.5", "k - means", "Метод опорных векторов", "Apriori",
            "EM", "PageRank", "AdaBoost", "kNN", "Наивный байесовский классификатор", "CART"]

f = open("algoritm.csv", "at")
nom_ = 1
for i in algoritm:
    f.write(str(nom_) + "," + i + "\n")
    nom_ += 1

f.close()
print("Файл создан")