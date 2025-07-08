import random
from colorama import Fore
database = {}


class BankAccount:
    def __init__(self, name="Dopont", balance=1000):
        self.name = name
        self.balance = balance

    def deposit(self, suma):
        self.balance += suma

    def retragerea(self, suma):
        if self.balance > suma:
            self.balance -= suma
            print(f"din contul dumneavoastră a fost sustras {suma} lei")
        else:
            print("balansa este mica")

    def sold(self):
        print(self.name, self.balance)


UserAccount = BankAccount(name="mihai", balance=2000)
UserAccount.deposit(100)
UserAccount.retragerea(350)
UserAccount.sold()


def generate():
    while True:
        pin = random.randint(1000, 9999)
        if pin not in database.keys():
            return pin
        else:
            continue


while True:
    ch = input(f"{Fore.GREEN} [1 access cont]  [2 create account]:  ")

    if ch == "1":
        while True:
            try:
                pin = int(input("Enter pin code: "))
                break
            except:
                print("pin is man bin number: ")
                continue

        if pin in database.keys():
            UserAccount = database[pin]
        else:
            print("user not found")
            continue

    elif ch == "2":
        while True:
            try:
                UserName = input("Enter Name: ")
                UserMoney = int(input("Enter First deposit : "))
                UserAccount = BankAccount(UserName, UserMoney)
                pin = generate()
                database.update({pin: UserAccount})
                print("account created with pin ", pin)
                break
            except:
                print("input data is not good")
                continue
    else:
        continue
    while True:
        operation = input(f"{Fore.GREEN} [1 withdrawal]: [ 2 sold]: [ 3 deposit]: [ 4 exiting and contined manipulation with your account]:  ")
        match operation:
            case "1":
                amount = input("[1 100]:  [2 200]:  [3 500]  [4 1000] : [5 2000] : [6 custom]: ")

                match amount:
                    case "1":
                        UserAccount.retragerea(100)
                    case "2":
                        UserAccount.retragerea(200)
                    case "3":
                        UserAccount.retragerea(500)
                    case "4":
                        UserAccount.retragerea(1000)
                    case "5":
                        UserAccount.retragerea(2000)
                    case "6":
                        UserAccount.retragerea(int(input("value: ")))

            case "2":
                UserAccount.sold()
            case "3":
                UserAccount.deposit(int(input("value: ")))
            case "4":
                break
            case _:
                print("command not found")
