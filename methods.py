import datetime
import pytz


class Account:
    """Simple account class with balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance  # '_Account__balance' will be used outside
        # of class because we have two underscores
        self._transaction_list = []
        print("Account created {}".format(self._name))
        if balance > 0:
            self._transaction_list.append((Account._current_time(), balance))

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print(
                "amount must be greater then 0 and less or equall then you have")
            self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposite"
            else:
                tran_type = "withdraw"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount,
                                                             tran_type,
                                                             date,
                                                             date.astimezone()))


if __name__ == '__main__':
    viktor = Account("Viktor", 0)
    viktor.show_balance()  # 0
    viktor.deposit(1000)
    viktor.withdraw(400)
    viktor.show_balance()  # 600
    viktor.show_transactions()

    steph = Account("Steph", 800)
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()
print(steph.__dict__)
