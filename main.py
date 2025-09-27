# This project was made by following Tech with Tim tutorials
# Source code: https://github.com/techwithtim/Python-Slot-Machine

import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

#change letter to emojis
symbol_count = {    #dictionary; how many times each symbol can appear
    "💎": 2,
    "🌸": 4, 
    "🍒": 6, 
    "🍰": 8
}

symbol_value = {    #dictionary; how much each symbol is worth
    "💎": 5,
    "🌸": 4,
    "🍒": 3,
    "🍰": 2
}

def show_rules():
    print("Welcome to slot_machine!! YAYYYYYAAYAY. 💎 = $5, 🌸 = $4, 🍒 = $3,  🍰 = $2")
    print("- deposit an amount of money")
    print("- bet on 1-3 lines (top, middle, bottom)") 
    print("- betting on 1 line = line 1, betting on 2 lines = lines 1 & 2, betting 3 lines = line 1, 2 & 3")
    print("- bets can be $1-$100")
    print("- matching symbols in the entire row win")
    print("- payout = symbol value * your bet")

show_rules()


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):   # checks each line the player bet on
        symbol = columns [0][line]  # take first column's symbol for this row
        for column in columns:              # check that symbol across all columns
            symbol_to_check = column[line] 
            if symbol != symbol_to_check:
                break   # stop checking columns if one doesn't match; user didn't win
        else:   #if symbols are the same, the user won
                winnings += values[symbol] * bet  #^^the user won the multiplier for the symbol times their bet (on each line, not total bet)
                winning_lines.append(line + 1)

    return winnings, winning_lines   #total amt user won, which lines they won

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]    #a copy of all_symbols
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns


def print_slot_machine(columns, winning_lines=[]):
    rows = len(columns[0])
    cols = len(columns)

    for row in range(rows):

        marker = "  \u2190 WIN!!!" if (row + 1) in winning_lines else ""
        print(f"Line {row + 1}: ", end="")  #titles each row

        for i, column in enumerate(columns):
            if i != cols - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print(marker)


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" +str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number a lines.")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: $ {balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print_slot_machine(slots, winning_lines)    # winning rows to be marked with an arrow 
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet #how much user won or lost from this spin

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break   #ends the game
        balance += spin(balance)

    print(f"You left with ${balance}")

main()


