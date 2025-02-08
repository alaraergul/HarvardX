def main():

    camel_case = input("Variable name in camel case: ").strip()
    snake_case = convert_to_snake_case(camel_case)

    print(snake_case)

def convert_to_snake_case(camel_case):

    snake_case_parts = []

    for char in camel_case:
        if char.isupper():
            if snake_case_parts:
                snake_case_parts.append('_')
            snake_case_parts.append(char.lower())
        else:
            snake_case_parts.append(char)
    return ''.join(snake_case_parts)

if __name__ == "__main__":
    main()
