# from accountant import *
# downloading_history_form_file()
# adding_to_history_from_terminal()
# working_on_the_data()
# print_balance()
# history = adding_to_history_from_terminal()
#
# file_path = "in.txt"
# file = open(file_path, 'w')
# for idx_1 in history:
#     for idx in idx_1:
#         file.write(str(idx) + "\n")
# file.write("stop" + '\n')

from decorators import *

manager.execute('saldo.py')
history = downloading_history_form_file(sys.argv[1])
print(history)
