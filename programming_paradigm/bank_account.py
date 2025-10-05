# bank_account.py
class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.__balance = float(initial_balance)  # encapsulated

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += float(amount)

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount <= self.__balance:
            self.__balance -= float(amount)
            return True
        return False

    def display_balance(self) -> None:
        # user-friendly print (2 decimal places)
        print(f"Current Balance: ${self.__balance:.2f}")

    def get_balance(self) -> float:
        # small accessor useful for automated tests
        return self.__balance
