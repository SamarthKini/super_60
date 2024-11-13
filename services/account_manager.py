from models.account import Account
from models.saving import Savings
from models.current import Current
from repositories.account_repository import AccountRepository
from exceptions.exceptions import * 
from services.transaction_manager import TransactionManger
from services.account_privileges_manager import AccountPriviligesManager



class AccountManager:
    def open_account(self,account_type,**kwargs):
        if account_type == 'savings':
            new_account = Savings(**kwargs)
        elif account_type == 'current':
            new_account = Current(**kwargs)
        else:
            raise ValueError("Invalid Account Type")
        
        AccountRepository.save_account(new_account)
        return new_account
    def check_account(self,account):
        if not account.is_active:
            raise AccountNotActiveException('Account is not Active')
        
    def validate_pin(self,account,pin_number):
        if account.pin_number != pin_number:
            raise InvalidPinException('Invalid Pin')
    
    def withdraw(self,account,amount,pin_number):
        self.check_account(account)
        self.validate_pin(account,pin_number)
        if account.balance < amount:
            raise InsufficientFundsExceptions('Insufficient Funds')
        
        account.balance -= amount
        TransactionManger.log_transaction(account.account_number,amount,'Withdraw')

    def deposit(self,account,amount):
        self.check_account(account)

        account.balance += amount
        TransactionManger.log_transaction(account.account_number,amount,'Deposit')

    def transfer(self, from_account, to_account, amount, pin_number):
        self.check_account(from_account)
        self.check_account(to_account)
        self.validate_pin(from_account,pin_number)

        
        if from_account.balance < amount:
            raise InsufficientFundsExceptions('Insufficient Funds')
        
        print(from_account.privilege)
        limit = AccountPriviligesManager.get_transfer_limit(from_account.privilege)
        if amount > limit:
            raise TransferLimitExceedException("Transfer limit exceeded")
        
        from_account.balance -= amount
        to_account.balance += amount
        TransactionManger.log_transaction(from_account.account_number,amount,'Transaction',to_account.account_number)

    def close_account(self,account):
        if not account.is_active:
            raise AccountNotActiveException('Account is already Deactivated')
        

        



    
