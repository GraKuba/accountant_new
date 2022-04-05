import sys

# GLOBAL VARIABLES

balance = 0
history = []
new_list = []
warehouse = {}
command = []
names = []
amounts = []


def downloading_history_form_file():
    global new_list
    file_path = "in.txt"
    file = open(file_path, 'r')

    while True:
        line = file.readline().strip()
        if line == "saldo":
            balance_change = file.readline().strip()
            comment = file.readline().strip()
            new_list = "saldo", balance_change, comment
            history.append(new_list)
            continue
        elif line == "zakup":
            product_name = file.readline().strip()
            product_price = file.readline().strip()
            number_of_items = file.readline().strip()
            balance_tuple = "zakup", product_name, product_price, number_of_items
            history.append(balance_tuple)
        elif line == "sprzedaz":
            product_name = file.readline().strip()
            product_price = file.readline().strip()
            number_of_items = file.readline().strip()
            balance_tuple = "sprzedaz", product_name, product_price, number_of_items
            history.append(balance_tuple)
        else:
            if line == "stop" or False:
                break
    return


def adding_to_history_from_terminal():
    action = sys.argv[0]
    if len(sys.argv) > 2:
        if action == "saldo.py":
            balance_change = int(sys.argv[1])
            comment = sys.argv[2]
            new_tuple = "saldo", balance_change, comment
            history.append(new_tuple)
        elif action == "zakup.py" or action == "sprzedaz.py":
            product_name = sys.argv[1]
            product_price = int(sys.argv[2])
            product_amount = int(sys.argv[3])
            if action == "zakup.py":
                action = "zakup"
            if action == "sprzedaz.py":
                action = "sprzedaz"
            new_tuple = action, product_name, product_price, product_amount
            history.append(new_tuple)
        elif action == "przeglad.py":
            number_of_commands = len(sys.argv)
            command_number = sys.argv[1:number_of_commands]
            for number in command_number:
                print(history[int(number)])
    return


def working_on_the_data():
    global command
    global balance
    global warehouse

    for command in history:
        if command[0] == "saldo":
            balance_change = int(command[1])
            if balance + balance_change < 0:
                print("Błąd. Za mało środków na koncie.")
                break
            balance += balance_change
        elif command[0] == "zakup":
            purchase_price = int(command[2]) * int(command[3])
            if balance < purchase_price:
                print("Błąd, nie stać cię na zakup.")
                break
            balance -= purchase_price
            if command[1] not in names:
                names.append(command[1])
                amounts.append(command[3])
            else:
                new_value = int(names.index(command[1])) + int(command[3])
                position = names.index(command[1])
                amounts[position] = int(amounts[position]) + new_value
            for idx in range(len(names)):
                warehouse[names[idx]] = amounts[idx]
        elif command[0] == "sprzedaz":
            sale_price = int(command[2]) * int(command[3])
            balance += sale_price
            for idx in names:
                if command[1] == idx:
                    position = names.index(idx)
                    amounts[position] = int(amounts[position]) - int(command[3])
            for idx_1 in range(len(names)):
                warehouse[names[idx_1]] = amounts[idx_1]
    return


def print_balance():
    print("Saldo: ", balance)
    return
