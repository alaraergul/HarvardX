import sys
import os
import csv
from tabulate import tabulate

def read_csv(filename):
    """Read CSV file and return the header and rows."""
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)
        rows = [row for row in reader]
    return header, rows

def print_table(header, rows):
    """Print table formatted as ASCII art using tabulate."""
    print(tabulate(rows, headers=header, tablefmt="grid"))

def main():
    if len(sys.argv) != 2:
        if len(sys.argv) < 2:
            print("Too few command-line arguments")
        else:
            print("Too many command-line arguments")
        sys.exit(1)

    filename = sys.argv[1]

    if not filename.endswith('.csv'):
        print("Not a CSV file")
        sys.exit(1)

    if not os.path.isfile(filename):
        print("File does not exist")
        sys.exit(1)

    header, rows = read_csv(filename)
    print_table(header, rows)

if __name__ == "__main__":
    main()
