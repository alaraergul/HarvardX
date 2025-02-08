def main():
    import sys

    names = []

    print("Enter names (press Ctrl-D to end):")
    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass

    if len(names) == 1:
        result = f"Adieu, adieu, to {names[0]}"
    elif len(names) == 2:
        result = f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        result = "Adieu, adieu, to " + ", ".join(names[:-1]) + ", and " + names[-1]

    print(result)

if __name__ == "__main__":
    main()
