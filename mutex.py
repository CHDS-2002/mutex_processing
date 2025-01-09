import os
import threading
from time import sleep
from random import randint
from threading import Lock

os.system('COLOR B')


class Bank:
    def __init__(self, balance: int, lock: Lock):
        self.balance = balance
        self.lock = lock

    def deposit(self):
        transactions = 100

        for t in range(transactions):
            f = randint(50, 500)
            self.balance += f
            print(f"Пополнение: {f}. Баланс: {self.balance}")

            if self.lock.locked() and self.balance >= 500:
                self.lock.release()

            sleep(0.001)

    def take(self):
        transactions = 100

        for t in range(transactions):
            f = randint(50, 500)
            print(f"Запрос на {f}")

            if f <= self.balance:
                self.balance -= f
                print(f"Снятие: {f}. Баланс: {self.balance}")
            else:
                print(f"Запрос отклонён, недостаточно средств")
                self.lock.acquire()

            sleep(0.001)


balance = 1  # Bitcoins)
lock = Lock()

bk = Bank(balance, lock)

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

try:
    os.system('PAUSE')
except:
    os.system('CLS')
