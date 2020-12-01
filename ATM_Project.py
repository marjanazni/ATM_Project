import datetime
import sys

def start_greeting():
    print("*******   HELLO, WELCOME TO ATM   *********\n",
          "***** ", datetime.datetime.now(), " *****\n")
start_greeting()

def end_greeting():
    print(" ")
    print("*******    THANK YOU FOR USING ATM    *******\n",
          "************     GOODBYE      **************\n")

accounts = {"1000111": "1111"}
# If user does not enter correct account number, he will not be allowed to move on to next step.
account_nr = input("ENTER YOUR ACCOUNT NR.:   ")

if account_nr in accounts:
    attempts = 0
    while attempts < 3:
        # User has 3 attempts to input correct pin, if failed, his account will be blocked.
        pin = input("ENTER YOUR PIN:   ")
        if pin == accounts[account_nr]:
            print("Login successful!")
            break
        else:
            print("Login failed!")
            attempts += 1
            print(3 - attempts, " attempts left.")
            if attempts == 3:
                print("Your account is blocked. Contact your ATM Branch.")
                end_greeting()
                sys.exit()
else:
    print("Account not found!")

    end_greeting()
    sys.exit()

decision = input("For PIN CHANGE press 1, for MONEY WITHDRAW press 2:    ")

def change_pin():
    pin_1 = input("ENTER YOUR PIN:   ")
    if pin == pin_1:
        print("Pin verified!")
    else:
        print("Pin not verified!")
        end_greeting()
        sys.exit()

    new_pin = input("ENTER NEW PIN:    ")
    accounts["1000111"] = new_pin
    while True:
        if len(new_pin) > 3 > len(new_pin):
            print("PIN Change failed!")
        else:
            print("PIN Change successful!")
            print(accounts)
            break

def withdraw_money_2():
    acc_bal_1000111 = int("5000")
    withdraw_amount = int(input("Enter withdraw amount:    "))
    new_bal_1000111 = acc_bal_1000111 - withdraw_amount

    if withdraw_amount < acc_bal_1000111 and acc_bal_1000111 > withdraw_amount:
        print("Transaction successful!\nNew balance on", datetime.datetime.now(), ":    ", new_bal_1000111, "EURO.")
        end_greeting()

    elif withdraw_amount > acc_bal_1000111 and acc_bal_1000111 < withdraw_amount:
        print("Enter lower withdraw amount.")
        withdraw_money()
    else:
        print(" ")

def withdraw_money():
    # User has 5.000 Euro in the bank account.
    acc_bal_1000111 = int("5000")
    withdraw_amount = int(input("Enter withdraw amount:    "))
    new_bal_1000111 = acc_bal_1000111 - withdraw_amount

    while True:

        if withdraw_amount <= acc_bal_1000111 and acc_bal_1000111 >= withdraw_amount:
            print("Transaction successful!\nNew balance on", datetime.datetime.now(), ":    ", new_bal_1000111, "EURO.")
            end_greeting()
            break

        elif withdraw_amount > acc_bal_1000111 and acc_bal_1000111 < withdraw_amount:
            print("Transaction failed!")
            withdraw_money_2()
            break
        else:
            print(" ")
            sys.exit()

if decision == "1":
    change_pin()
elif decision == "2":
    withdraw_money()
else:
    print("Wrong entry.")
    end_greeting()