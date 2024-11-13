from models.privileges import AccountPrivileges
class AccountPriviligesManager:
    priviliges = {
        'PREMIUM' : 100000,
        'GOLD' : 50000,
        'SILVER' : 25000
    }
    @classmethod
    def get_transfer_limit(cls,privilige):
        return cls.priviliges.get(privilige,0)
    
