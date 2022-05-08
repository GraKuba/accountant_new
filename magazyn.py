from decorators import *
working_on_the_data()

warehouse = working_on_the_data()[1]

for position in warehouse:
    print(f"Name: {position} | Amount: {warehouse[position]}")
