# cash.py

def get_change_owed():
    while True:
        try:
            change = float(input("Change owed: "))
            if change >= 0:
                return change
            else:
                print("Please enter a non-negative value.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")


def calculate_coins(change):
    coins = 0
    cents = round(change * 100)

    # Calculate the number of quarters
    coins += cents // 25
    cents %= 25

    # Calculate the number of dimes
    coins += cents // 10
    cents %= 10

    # Calculate the number of nickels
    coins += cents // 5
    cents %= 5

    # Calculate the number of pennies
    coins += cents

    return coins


def main():
    change = get_change_owed()
    coins = calculate_coins(change)
    print(coins)


if __name__ == "__main__":
    main()
