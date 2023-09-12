
balance = 0
history = []


def check_balance():
    print(f"Ваш текущий баланс: {balance} рублей")


def withdraw(money):
    global balance  
    if money > 0 and money <= balance:
        balance -= money
        print(f"Вы сняли {money} рублей")
        history.append(f"Снятие: {money} рублей")
    else:
        print("Недостаточно средств на счете")


def deposit(amount):
    global balance     
    if amount > 0:
        balance += amount
        print(f"Вы пополнили счет на {amount} рублей")
        history.append(f"Пополнение: {amount} рублей")
    else:
        print("Некорректная сумма для пополнения")


def hist():
    print("История операций:")
    for transaction in history:
        print(transaction)


check_balance()
deposit(int(input('Сколько рублей хотите внести:')))
withdraw(int(input('Сколько хотите снять:')))
hist()
