def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money : # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원 입니다.".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100 # 수수료 100원
    return commission, balance - money - commission

balance = 0
balance123 = 1000
balance1 = deposit(1000, 1000)
balance123 = deposit(balance123, 10000)
print(balance1)
print(balance123)

commission, balance123 = withdraw_night(balance123, 10000)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance123))