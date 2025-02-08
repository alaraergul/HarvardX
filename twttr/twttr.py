def main():

    text = input("Text: ").strip()

    vowels = "aeiouAEIOU"

    result = ''.join(char for char in text if char not in vowels)

    print(result)

if __name__ == "__main__":
    main()
