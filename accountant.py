import sys


def downloading_history_form_file():
    history = []
    file_path = "in.txt"
    file = open(file_path, 'r')

    while True:
        line = file.readline().strip()
        if line == "saldo":
            balance_change = file.readline().strip()
            comment = file.readline().strip()
            temp_list = "saldo", balance_change, comment
            history.append(temp_list)
            continue
        elif line == "zakup":
            product_name = file.readline().strip()
            product_price = file.readline().strip()
            number_of_items = file.readline().strip()
            temp_list = "zakup", product_name, product_price, number_of_items
            history.append(temp_list)
        elif line == "sprzedaz":
            product_name = file.readline().strip()
            product_price = file.readline().strip()
            number_of_items = file.readline().strip()
            temp_list = "sprzedaz", product_name, product_price, number_of_items
            history.append(temp_list)
        else:
            if line == "stop" or False:
                break
    return history


def adding_to_history_from_terminal():
    history = downloading_history_form_file()
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
    return history


def working_on_the_data():
    history = adding_to_history_from_terminal()
    command = []
    balance = 0
    warehouse = {}
    names = []
    amounts = []

    for command in history:
        if command[0] == "saldo":
            balance_change = int(command[1])
            if balance + balance_change < 0:
                print("B????d. Za ma??o ??rodk??w na koncie.")
                break
            balance += balance_change
        elif command[0] == "zakup":
            purchase_price = int(command[2]) * int(command[3])
            if balance < purchase_price:
                print("B????d, nie sta?? ci?? na zakup.")
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
    return balance, warehouse


def print_balance():
    balance = working_on_the_data()[0]
    print("Saldo: ", balance)
    return
