from decorators import *
history = downloading_history_form_file(sys.argv[1])

number_of_commands = len(sys.argv)
command_number = sys.argv[2:number_of_commands]
for number in command_number:
    print(history[int(number)])
