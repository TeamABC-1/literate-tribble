import random

MAX_LINE = 3
MAX_BET = 100
MIN_BET= 1

ROWS = 3
COLS = 3

symbol_count={  #creating a dictionary 
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value={ 
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winning(columns, lines, bet, vlaues):
    winnigns=0
    winnign_lines = [] 
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnigns += vlaues[symbol] * bet
            winnign_lines.append(lines + 1)

    return winnigns, winnign_lines
            


def get_solt_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):  #anonymous variable in pyhton
                all_symbols.append(symbol)

    columns =[]
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:] #slicing the list/ to copy
        for row in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value) # so that we don't pick up that again like we have defined 2A to avoid selection of  3A or more
            column.append(value)

        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end=" | ") # to print the pipe in the middle not at the end
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount=input("What would you like to depost? $ ")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please Enter a amount.")
    return amount

def get_number_of_line():
    while True:
        lines=input(" Enter the number of line to bet on (1-" + str(MAX_LINE) + ")? ")
        if lines.isdigit():
            lines=int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print("Enter a Valid number of lines. ")
        else:
            print("Please Enter a amount.")

    return lines

def get_bet():
    while True:
        amount=input("What would you like to each bet? $ ")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print(f"Amount must be between{MIN_BET} -${MAX_BET} .") #can print variable available only in python 3 and above
        else:
            print("Please Enter a amount.")
    return amount

def spin(balance):
    #balance = deposit()
    lines= get_number_of_line()
    while True:
        bet=get_bet()
        total_bet= bet * lines

        if total_bet > balance:
            print(f"You do Not have enough to bet that amount, your current balance is: ${balance}")

        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to : $ {total_bet} ")
    
    slots = get_solt_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winning(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}. ")
    print(f"You won on lines: ", *winning_lines) #splat function
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current Balance is ${balance}")
        answer = input("Press enter to Play (q to quit.)")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")

main()