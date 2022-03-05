class Atm:
    def __init__(self, name, balance, pin):
        self.name = name
        self.balance = balance
        self.pin = pin

    def displayBalance(self):
        print('You have $'+str(self.balance)+' in the bank')

    def withDraw(self):
        yourpin = int(input('Enter your pin '))
        if(self.pin == yourpin):
            money = int(input('Enter the amount that you want to draw '))
            if(money <= self.balance):
                self.balance = self.balance-money
                print('$'+str(money)+' is drawn. It left $'+str(self.balance))
            elif(money > self.balance):
                print('You wrote too much money. Try again')
        else:
            print("It's not your pin. Try it in 5 seconds.")
    def deposit(self):
        yourpin = int(input('Enter your pin '))
        if(self.pin == yourpin):
            money = int(input('Enter the amount that you want to deposit '))
            if(money <= self.balance):
                self.balance = self.balance+money
                print('$'+str(money)+' is deposited. It left $'+str(self.balance))
        else:
            print("It's not your pin. Try it in 5 seconds.")
Minho = Atm('Minho',500,1234)
Minho.deposit()