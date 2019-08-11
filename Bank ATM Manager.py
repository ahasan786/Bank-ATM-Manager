#BankAccountProject

#Title of Project: Bank Account ATM Manager
#Created by: Ali Hasan


#Welcome Message
def verify_id():
    if verify_id == '1234':
        return True
    else:
        return False

def log_in():
    tries = 0
    while tries < 4:
        id = input(int("Please input your four digit ID number: "))
        if verify_id(id):
            print("ID accepted!")
            return True
        else:
            print("Invalid ID, please try again")
            tries += 1
        print("Too many tries, you are locked out please try again later")
        return False

def start_menu():
    print("Welcome to the start menu")
    if log_in():
        user_response = input(str("Please select the action using the corresponding number you want to do today: "
                              "1) Show Account Details"
                              "2) Go to Savings Account"
                              "3) Go to Checking Account"
                              "4) Go to Business Account"
                              "5) Add Account"
                              "6) Exit"))
    elif user_response == '6':
        print("Exiting program, have a nice day!")
    else:
        return False


class bank_account:
    accounts = [] #Find a way on how to incooperate past accounts

    def __init__(self, first, last, id_num):
        self.first = first
        self.last = last
        self.id_num = id_num

    def add_acct(self, add):
        if user_response = 'Add Account':
            type = input(str("What type of account would you like to open?"))
            if type.lower == "checking":
                self.accounts.append(add)
            elif type.lower == 'savings':
                self.accounts.append(add)
            else:
                return None

    def del_acct(self, delete_acct):
        if user_response = 'Delete Account':
            type_2 = input(str(What account would you like to delete? "))
            if type_2.lower == "checkings":
                self.accounts.remove(delete_acct)
            elif type_2.lower == "savings":
                self.accounts.remove(delete_acct)

class checking_account(bank_account):
    def __init__(self, first, last, id_num, check_bal_amt):
        bank_account.__init__(self, first, last, id_num)
        self.check_bal_amt = check_bal_amt
    def withdrawal(self, wd_amt):
        if wd_amt < self.check_bal_amt:
            self.check_bal_amt -= wd_amt
            print("You have sucessfully withdrawn {} and have a balance of {}". format(wd_amt, self.check_bal_amt))
        else:
            print("You do not have enough money to withdrawal this amount")
    def deposit(self, depos_amt):
        if depos_amt > 1:
            self.bal_amt += depos_amt
    def show_balance(self):
        print("Here is the present balance for your savings account {}: {}".format(self.first,self.bal_amt))

class savings_account(bank_account):
    def __init__(self, first, last, id_num, save_bal_amt):
        bank_account.__init__(self, first, last, id_num)
        self.save_bal_amt = save_bal_amt
    def

class business_account(bank_account):
    def __init__(self, first, last, id_num, buss_bal_amt):
        bank_account.__init__(self, first, last, id_num)