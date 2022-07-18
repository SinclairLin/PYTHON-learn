class BankAccount:

    def __init__(self, user_name, user_account):
        self.user_name = user_name
        self.user_account = user_account
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


my_account = BankAccount("聂哥", 114514)
print('Hello! ', my_account.user_name, my_account.user_account)
while 1:
    my_account.ff()
