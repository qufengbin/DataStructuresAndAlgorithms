class CreditCard:
    """信用卡消费者"""

    def __init__(self,customer,bank,acnt,limit):
        """
        创建一个新的信用卡实例。初始消费额（balance）是 0
        customer：消费者姓名
        bank：银行
        acnt：卡号
        limit：信用卡限额
        """

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self,price):
        """
        :param price: 消费额
        :return: True说明本次消费允许；False说明本次消费不允许
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self,amount):
        self._balance -= amount

if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('Tom','ACBC','123456789',2500))
    wallet.append(CreditCard('Jim','ACB','456789123',3500))
    wallet.append(CreditCard('Jack','ACBC','789456123',5000))

    for val in range(1,17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print('Customer = ', wallet[c].get_customer())
        print('Bank = ', wallet[c].get_bank())
        print('Account = ', wallet[c].get_account())
        print('Limit = ', wallet[c].get_limit())
        print('Balance = ', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New Balance =', wallet[c].get_balance())
            print()