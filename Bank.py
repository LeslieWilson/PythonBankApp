


def withdraw(input, amount):
    if input == "savings":
        savings = open("savings.txt", 'r').read()
        savings = int(savings)
        savings -= amount
        file = open("savings.txt", "w").write(str(savings))
    elif input == "checking":
        checking = open("checking.txt", 'r').read()
        checking = int(checking)
        checking -= amount
        file = open("checking.txt", "w").write(str(checking))


def deposit(input, amount):
    if input == "savings":
        savings = open("savings.txt", 'r').read()
        savings = int(savings)
        savings += amount
        file = open("savings.txt", "w").write(str(savings))
    elif input == "checking":
        checking = open("checking.txt",'r').read()
        checking = int(checking)
        checking += amount
        file = open("checking.txt", "w").write(str(checking))

def transfer (input, amount):
    if input == "savings":
        savings = open("savings.txt", 'r').read()
        savings = int(savings)
        savings -= amount
        file = open("savings.txt", "w").write(str(savings))
        checking = open("checking.txt", 'r').read()
        checking = int(checking)
        checking += amount
        file = open("checking.txt", "w").write(str(checking))

    elif input == "checking":
        checking = open("checking.txt", 'r').read()
        checking = int(checking)
        checking -= amount
        file = open("checking.txt",'w').write(str(checking))
        savings = open("savings.txt","r").read()
        savings = int(savings)
        savings += amount
        file = open("savings.txt", "w").write(str(savings))


print("what account do you want to use")
account = input()
print("ok, what do you want to do? choose transfer, deposit, withdraw")
action = input()
print("how much money do you want to move? give an integer")
amount = input()
amount = (int(amount))


if action == "transfer" and account == "savings":
    transfer(account, amount)
elif action == "transfer" and account == "checking":
    transfer(account, amount)

elif account == 'savings' and action == "deposit":
    deposit(account,amount)

elif account == 'savings' and action == "withdraw":
    withdraw(account,amount)

elif account == "checking" and action == "deposit":
    deposit(account,amount)

elif account == "checking" and action == "withdraw":
    withdraw(account,amount)
