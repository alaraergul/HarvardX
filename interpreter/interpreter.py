def main():

    expression = input("Expression: ").strip()

    x, operator, z = expression.split()

    x = int(x)
    z = int(z)

    if operator == "+":
        result = x + z
    elif operator == "-":
        result = x - z
    elif operator == "*":
        result = x * z
    elif operator == "/":
        result = x / z

    print(f"{result:.1f}")

if __name__ == "__main__":
    main()
