momo_account = {
    '0244857468': {'balance': 100, 'pin': '5043', 'name': 'Yaw Boakye'},
    '0244687889': {'balance': 700, 'pin': '2638', 'name': 'Ama Obeng'}
}
account_1 = momo_account['0244857468']
account_2 = momo_account['0244687889']

"""def deposit(phone,amount):
    account = momo_account[phone]
    momo_account[deposit_num]['balance'] += amount
    print(account)

deposit_num = input("Enter your mobile number : ")

if deposit_num in momo_account:
    deposit_amt = input("Enter deposit amount : ")
    eval_deposit_amt = eval(deposit_amt)
    deposit(deposit_num, eval_deposit_amt)
else:
    print("The number is not registered")"""



"""def withdraw(phone,amount,pin):
    account = momo_account[phone]
    momo_account[withdraw_num]['balance'] -= amount
    if pin == momo_account[withdraw_num]['pin']:
        print(account)
    else:
        print("The pin is in correct")



withdraw_num = input("Enter your mobile number ")

if withdraw_num in momo_account:
    withdraw_amt = input("Enter withdrawal amount : ")
    eval_withdraw_amt = eval(withdraw_amt)
    withdraw_pin = input("Enter your pin ")
    withdraw(withdraw_num, eval_withdraw_amt, withdraw_pin)

else:
    print("The number is not registered")"""






def transfer(phone,amount,pin,transnum):
    account = momo_account[phone],\
              momo_account[transnum]
    momo_account[phone_num]['balance'] -= amount
    momo_account[transfer_num]['balance'] += amount
    if pin == momo_account[phone_num]['pin']:
        print(account)
    else:
        print("The pin is in correct")


phone_num = input("Enter your mobile number: ")
transfer_num = input("Enter transfer number: ")

if  phone_num in momo_account or transfer_num in momo_account:
    transfer_amt = input("Enter transfer amount: ")
    eval_transfer_amt = eval(transfer_amt)
    transfer_pin = input("Enter your pin: ")
    transfer(phone_num, eval_transfer_amt, transfer_pin,transfer_num)

else:
    print("The number is not registered")




