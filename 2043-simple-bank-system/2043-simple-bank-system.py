class Bank:

    def __init__(self, balance: List[int]):
        self.accounts = [0] + balance
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 < 1 or account2 < 1 or account1 >= len(self.accounts) or account2 >= len(self.accounts):
            return False
        if self.accounts[account1] - money < 0:
            return False
        self.accounts[account1] -= money
        self.accounts[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account < 1 or account >= len(self.accounts):
            return False
        self.accounts[account] += money
        return True
        

    def withdraw(self, account: int, money: int) -> bool:
        if account < 1 or account >= len(self.accounts):
            return False
        if self.accounts[account] - money < 0:
            return False
        self.accounts[account] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)