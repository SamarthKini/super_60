class AccountRepository:
    #class attribute to keep track of all accounts
    accounts:list = []
    account_counter:int = 1000

    #Method to generate a new account number
    @classmethod
    def generate_account_number(cls) -> int:
        cls.account_counter += 1
        return cls.account_counter

    #Method to save an account
    @classmethod
    def save_account(cls, account) -> None:
        cls.accounts.append(account)

    #Method to get all accounts
    def get_all_accounts(self) -> list:
        return self.accounts
