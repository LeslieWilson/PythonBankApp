


def withdraw(input, amount):
    if input == "savings":
        savings = open("savings.txt", 'r').read()
        savings = int(savings)
        savings -= amount
    elif input == "checking":
        checking = open("checking.txt", 'r').read()
        checking = int(checking)
        checking -= amount


def deposit(input, amount):
    if input == "savings":
        savings = open("savings.txt", 'r').read()
        savings = int(savings)
        savings += amount
    elif input == "checking":
        checking = open("checking.tandhxt",'r').read()
        checking = int(checking)
        checking += amount

def transfer (input, amount):
    if input == "savings":
        savings = open("savings.txt", 'r').read()
        savings = int(savings)
        savings -= amount
        file = open("savings.txt", "w").write(str(savings))










        checking = open("checking.txt", 'r').read()
        checking = int(checking)
        checking += amount
    elif input == "checking":
        checking = ("checking.txt", 'r').read()
        checking = int(checking)
        checking -= amount
        savings = open ("savings.txt",'r').read()
        savings = int(savings)
        saving += amount


print("what account do you want to use")
account = input()
print("ok, what do you want to do? choose transfer, deposit, withdraw")
action = input()
print("how much money do you want to move? give an integer")
amount = (int(input())


if action == "transfer" and account == "savings":
    transfer("savings", amount)
elif action == "transfer" and account == "checking":
    transfer("checking", amount)








#         File.open("Bank.txt", 'w')
#         opened_file= file.write(savings)
#     elif input == "checking":
#         checking -= amount
#
#
# withdraw("savings", 40)
