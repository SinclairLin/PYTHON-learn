class BankAccount:

    def __init__(self, userName, userAccount):
        self.userName = userName
        self.userAccount = userAccount
        self.balance = 0.0

    def PrintBalance(self):  # print 余额
        print('Your balance is ', self.balance)

    def Save(self):  # 存
        print('Please enter a number: ')
        self.balance += float(input())

    def Withdraw(self):  # 取
        print('Please enter a number: ')
        self.balance -= float(input())

    def ff(self):
        print('enter a num: ')
        print('1.Balance')
        print('2.Save')
        print('3.Withdraw')
        flag = int(input())
        if flag == 1:
            myAccount.PrintBalance()
        elif flag == 2:
            myAccount.Save()
            myAccount.PrintBalance()
        elif flag == 3:
            myAccount.Withdraw()
            myAccount.PrintBalance()
        else:
            print('error')


myAccount = BankAccount("聂哥", 114514)
print('Hello! ', myAccount.userName, myAccount.userAccount)
while 1:
    myAccount.ff()
