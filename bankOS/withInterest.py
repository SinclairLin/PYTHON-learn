class BankAccount:

    def __init__(self, user_name, user_account):
        self.user_name = user_name
        self.user_account = user_account
        self.userName = user_name
        self.userAccount = user_account
        self.balance = 0.0

    def print_balance(self):  # print 余额
        print('Your balance is ', self.balance)

    def save(self):  # 存
        print('Please enter a number: ')
        self.balance += float(input())

    def withdraw(self):  # 取
        print('Please enter a number: ')
        self.balance -= float(input())

    def ff(self):  # 主控
        print('enter a num: ')
        print('1.Balance')
        print('2.Save')
        print('3.Withdraw')
        flag = int(input())
        if flag == 1:
            my_account.print_balance()
        elif flag == 2:
            my_account.save()  # 存
            my_account.print_balance()
        elif flag == 3:
            my_account.withdraw()
            my_account.print_balance()
        else:
            print('error')


class InterestAccount(BankAccount):  # 继承BankAccount 类


    def save(self):    # 对父类的save 方法进行重构

    def __init__(self, user_name, user_account):
        super().__init__(user_name, user_account)
        self.user_name = user_name
        self.user_account = user_account
        self.balance = 0.0
        
    def save(self): 
        interest = 0.05  # 年利率
        print('存多少: ')
        self.balance += float(input())
        print('存多久?(年)')
        save_years = int(input())
        self.balance = self.balance * (1.0 + interest * save_years)  # 计算X年后余额
        print(save_years,' 年后,余额为: ',self.balance)


    # def add_interest(self):  # 计算利息
    #     self.Interest = 0.05
    #     print('存多久(单位:年)')  # 键入存取时间(年)
    #     self.saveyears = int(input())
    #     self.balance = self.balance * (1 + self.Interest) * self.saveyears
    #     print(self.saveyears, ' 年后,余额为: ', self.balance)


my_account = InterestAccount('聂哥', 114514)
while 1:
    my_account.ff()
