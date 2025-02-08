def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    if not (2 <= len(s) <= 6):
        return False


    if not (s[0].isalpha() and s[1].isalpha()):
        return False


    if not s.isalnum():
        return False


    i = 0
    while i < len(s) and s[i].isalpha():
        i += 1

    if i < len(s):
       
        if s[i:].isdigit() and (s[i] != '0'):
            return True
        else:
            return False

    return True

if __name__ == "__main__":
    main()
