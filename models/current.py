from models.account import Account


class Current(Account):
    def __init__(self, name: str, balance: int, privilege: str, pin_number: int, registration_number:int, website_url:str) -> None:
        super().__init__(name, balance, privilege, pin_number)
        self.registration_number = registration_number
        self.website_url = website_url