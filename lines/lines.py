import sys
import os

def count_lines_of_code(filename):
    """Count non-blank, non-comment lines in a Python file."""
    with open(filename, 'r') as file:
        lines = file.readlines()

    loc = 0
    for line in lines:
        stripped_line = line.strip()
        # Check if line is not blank and does not start with '#'
        if stripped_line and not stripped_line.startswith('#'):
            loc += 1
    return loc

def main():
    # Check if exactly one command-line argument is provided
    if len(sys.argv) != 2:
        if len(sys.argv) < 2:
            print("Too few command-line arguments")
        else:
            print("Too many command-line arguments")
        sys.exit(1)

    filename = sys.argv[1]

    # Check if the file has a .py extension
    if not filename.endswith('.py'):
        print("Not a Python file")
        sys.exit(1)

    # Check if the file exists
    if not os.path.isfile(filename):
        print("File does not exist")
        sys.exit(1)

    # Count the lines of code in the file
    loc = count_lines_of_code(filename)
    print(loc)

if __name__ == "__main__":
    main()
