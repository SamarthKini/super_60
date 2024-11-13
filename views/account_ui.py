from services.account_manager import AccountManager
from services.transaction_manager import TransactionManger
from repositories.account_repository import AccountRepository


class AccountUI:
    def start(self):
        while True:
            print('''\n\n\nWelcome to Global Digital Bank
Select an option
1. Open Account
2. Close Account
3. Withdraw Funds
4. Deposit Funds
5. Transfer Funds
9. Exit
''')
            choice = int(input('Enter your choice: '))

            match choice:
                case 1:
                    self.open_account()
                case 2:
                    self.close_account()
                case 3:
                    self.withdraw_funds()
                case 4:
                    self.deposit_funds()
                case 5:
                    self.transfer_funds()
                case 9:
                    pass
                case _:
                    print('Invalid choice, Please Try Again!')
    def open_account(self):
        account_type = input('Enter the account type (saving/current): ').strip().lower()
        name = input("Enter your name: ")
        amount = float(input("Enter initial deposit amount: "))
        pin_number = int(input("Enter your pin number: "))
        privilege = input("Enter the account privilege (PREMIUM/GOLD/SILVER): ").strip().lower()
        
        if account_type == 'saving':
            date_of_birth = input('Enter your date of birth (YYYY-MM-DD): ')
            gender = input('Enter your gender (M/F): ')
            account  = AccountManager().open_account(account_type, name=name, balance=amount,date_of_birth = date_of_birth, pin_number=pin_number, privilege=privilege, gender = gender)

        elif account_type == 'current':
            registration_number = input('Enter your registration number: ')
            website_url = input('Enter your website url: ')
            account = AccountManager().open_account(account_type, name=name, balance=amount,
                    registration_number=registration_number, website_url=website_url, pin_number=pin_number,
                    privilege=privilege)
        
        else:
            print('Invalid account type. Please Try Again!')
        
        print(account_type.capitalize(),"Account opened succesfully. Account Number: ",account.account_number)
        
    def close_account(self):
        account_number = int(input('Enter your account number: '))
        account = next((acc for acc in AccountRepository.accounts if acc.account_number == account_number))

        if account:
            try:
                AccountManager().close_account(account)
                print('Account closed successfully')
            except Exception as e:
                print("Error: ",e)
        else:
            print('Account Not Found.Please try again')

    def withdraw_funds(self):
        account_number = int(input('Enter your account number: '))
        amount = float(input("Enter amount to withdraw: "))
        pin_number = int(input("Enter your pin number: "))
        account = next((acc for acc in AccountRepository.accounts if acc.account_number == account_number))
        if account:
            try:
                AccountManager().withdraw(account, amount, pin_number)
            except Exception as e:
                print('Error: ', e)
        else:
            print("Account not found. Please try again")

        
            

    def deposit_funds(self):
        account_number = int(input("Enter your account number: "))
        amount = float(input("Enter the amount to deposit: "))
        account  = next((acc for acc in AccountRepository.accounts if acc.account_number == account_number), None)

        if account:
            try:
                AccountManager().deposit(account, amount)
                print("Amount deposited successfully")
            except Exception as e:
                print('Error: ', e)
        else:
            print("Account not found. Please try again")

    
    def transfer_funds(self):
        account_number_receiver = int(input("Enter your account numberof the receiver: "))
        account_number_sender = int(input("Enter your account number of the sender: "))
        amount = float(input("Enter the amount to deposit: "))
        pin_number = int(input("Enter your pin number: "))
        from_account  = next((acc for acc in AccountRepository.accounts if acc.account_number == account_number_sender), None)
        to_account = next((acc for acc in AccountRepository.accounts if acc.account_number == account_number_receiver), None)
        if from_account and to_account:    
            try:
                AccountManager().transfer(from_account, to_account, amount, pin_number)
                print(f'Funds worth ₹{amount} were successfully transferred from {account_number_sender} to {account_number_receiver}')
            except Exception as e:
                print(f'Error: {e}')
        else:
            print('Invalid account credentials. Please verify and try agian')
