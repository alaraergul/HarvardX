def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total_cost = 0.0

    try:
        while True:

            item = input("Item: ").strip()
            normalized_item = item.title()

            if normalized_item in menu:

                total_cost += menu[normalized_item]

            print(f"Total: ${total_cost:.2f}")

    except EOFError:
        pass

if __name__ == "__main__":
    main()
