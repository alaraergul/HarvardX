import re

def validate(ip):
    # Regular expression to match a valid IPv4 address
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.match(pattern, ip)

    if match:
        # Check if all four parts are between 0 and 255
        return all(0 <= int(part) <= 255 for part in match.groups())
    return False

def main():
    ip = input("IPv4 Address: ")
    if validate(ip):
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()
