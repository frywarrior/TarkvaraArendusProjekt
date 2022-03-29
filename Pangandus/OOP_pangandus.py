# Franco Kikkas IS21

class User:
    def __init__(self, name, sirname, age, gender):
        self.name = name
        self.sirname = sirname
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Konto Detailid\n")
        print("Nimi ", self.name, self.sirname)
        print("Vanus  ", self.age)
        print("Sugu ", self.gender)


class Bank(User):
    def __init__(self, name, sirname, age, gender, pin="0000", balance=0):
        super().__init__(name, sirname, age, gender)
        self.pin = str(pin)
        self.balance = balance

    def deposit(self, amount):
        x = str(input("\nSisestage oma kood : "))
        if x == self.pin:
            print("Kood on õige!")
            self.balance = self.balance + amount
            print("Konto summa on muudetud : €", self.balance)
        else:
            print("Vale Kood!")
            print("Palun proovige uuesti!")

    def withdraw(self, amount):
        x = str(input("\nSisestage oma kood : "))
        if x == self.pin:
            print("Kood on õige!")
            if amount > self.balance:
                print("Kontol liiga vähe raha | Raha on teil : €", self.balance)
            else:
                self.balance = self.balance - amount
                print("Konto summa on muudetud : €", self.balance)
        else:
            print("Vale Kood!")
            print("Palun proovige uuesti!")

    def view_balance(self):
        self.show_details()
        print("Konto raha: €", self.balance)


def find(fn, f1, f2):
    file1 = open(fn, "r")

    for line in file1:
        ajutine = eval(line.strip())
        if ajutine['name'] == f1 and ajutine['sirname'] == f2:
            x = 1
            return x, ajutine

    file1.close()
    return 0, 0


def replace(fn, x):
    x = vars(x)
    file = open(fn, "r")
    data = file.readlines()
    u = 0
    for i in data:
        i = i.removesuffix('\n')
        i = eval(i)
        if i['name'] == x['name'] and i['sirname'] == x['sirname']:
            b = u
        u += 1

    x = str(x) + "\n"
    data[b] = x

    with open(fn, 'w') as file:
        file.writelines(data)


def new(fn, x):
    x = str(vars(x)) + "\n"
    with open(fn, 'a') as file:
        file.write(x)
