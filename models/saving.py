from models.account import Account


class Savings(Account):
    def __init__(self, name: str, balance: int, privilege: str, pin_number: int, date_of_birth:str, gender:str):
        super().__init__(name, balance, privilege, pin_number)
        self.date_of_birth = date_of_birth
        self.gender = gender
        #self.isActive = is_active