def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split('/')
            x = int(x)
            y = int(y)

            if y == 0 or x > y:
                print("Invalid fraction. Try again.")
                continue

            percentage = round((x / y) * 100)

            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break

        except (ValueError, ZeroDivisionError):
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()
