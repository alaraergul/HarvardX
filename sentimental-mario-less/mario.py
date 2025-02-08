
def get_height():
    while True:
        try:
            height = int(input("Height: "))
            if height > 0 and height <= 8:
                return height
            else:
                print("Height must be a positive integer between 1 and 8, inclusive.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def print_pyramid(height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        blocks = "#" * i
        print(spaces + blocks)


def main():
    height = get_height()
    print_pyramid(height)


if __name__ == "__main__":
    main()
