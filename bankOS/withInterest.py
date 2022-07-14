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

    def ff(self):    # 主控
        print('enter a num: ')
        print('1.Balance')
        print('2.Save')
        print('3.Withdraw')
        flag = int(input())
        if flag == 1:
            myAccount.PrintBalance()
        elif flag == 2:
            myAccount.Save()    # 存
            myAccount.PrintBalance()
        elif flag == 3:
            myAccount.Withdraw()
            myAccount.PrintBalance()
        else:
            print('error')


class InterestAccount(BankAccount):  # 继承BankAccount 类

    def __init__(self, userName, userAccount):
        super().__init__(userName, userAccount)
        self.userName = userName
        self.userAccount = userAccount
        self.balance = 0.0

    def Save(self):
        intrest = 0.05    # 年利率
        print('存多少: ')
        self.balance += float(input())
        print('存多久?(年)')
        save_years = int(input())
        self.balance = self.balance * (1.0 + intrest) * save_years    # 计算X年后余额
        print(save_years,' 年后,余额为: ',self.balance)

    # def addIntrest(self):  # 计算利息
    #     self.Interest = 0.05
    #     print('存多久(单位:年)')  # 键入存取时间(年)
    #     self.saveyears = int(input())
    #     self.balance = self.balance * (1 + self.Interest) * self.saveyears
    #     print(self.saveyears, ' 年后,余额为: ', self.balance)


myAccount = InterestAccount('聂哥', 114514)
while 1:
    myAccount.ff()
