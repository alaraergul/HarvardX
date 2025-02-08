def main():

    calories = {
        "Apple": 130,
        "Avocado": 50,
        "Banana": 110,
        "Blueberries": 80,
        "Cherries": 50,
        "Grapefruit": 60,
        "Grapes": 90,
        "Kiwi": 40,
        "Kiwifruit": 90,
        "Lemon": 20,
        "Lime": 20,
        "Mango": 150,
        "Nectarine": 60,
        "Orange": 80,
        "Peach": 60,
        "Pear": 100,
        "Pineapple": 80,
        "Plum": 70,
        "Raspberry": 60,
        "Strawberries": 50,
        "Sweet Cherries": 100,
        "Watermelon": 80
    }


    fruit = input("Fruit: ").strip()

    fruit = fruit.title()

    if fruit in calories:
        print(f"Calories: {calories[fruit]}")
    else:

        pass

if __name__ == "__main__":
    main()
