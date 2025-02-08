def main():

    total_inserted = 0
    amount_due = 50

    while total_inserted < amount_due:

        coin = int(input("Insert Coin: ").strip())


        if coin in {25, 10, 5}:
            total_inserted += coin

            if total_inserted < amount_due:
                print(f"Amount Due: {amount_due - total_inserted}")
        else:

            print(f"Amount Due: {amount_due - total_inserted}")

    change_owed = total_inserted - amount_due
    print(f"Change Owed: {change_owed}")

if __name__ == "__main__":
    main()
