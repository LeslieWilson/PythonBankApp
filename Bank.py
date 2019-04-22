

print("what do you want")
user_input = input()


def withdraw(input, amount):

    if input == "savings":
        savings = open("savings.txt", 'r').read()
        savings = int(savings)
        savings -= amount



        File.open("Bank.txt", 'w')
        opened_file= file.write(savings)
    elif input == "checking":
        checking -= amount


withdraw("savings", 40)
