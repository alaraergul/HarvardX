import sys
import csv

def split_name(name):
    """Split a full name into first and last names."""
    parts = name.split(', ')
    if len(parts) != 2:
        raise ValueError("Name format is incorrect")
    last_name, first_name = parts
    return first_name, last_name

def process_csv(input_filename, output_filename):
    """Read from input CSV and write to output CSV with names split."""
    try:
        with open(input_filename, mode='r') as infile:
            reader = csv.reader(infile)
            header = next(reader)
            if header != ['name', 'house']:
                raise ValueError("Input CSV header is incorrect")

            rows = []
            for row in reader:
                name, house = row
                first_name, last_name = split_name(name)
                rows.append([first_name, last_name, house])

    except FileNotFoundError:
        print(f"Could not read {input_filename}")
        sys.exit(1)
    except ValueError as e:
        print(e)
        sys.exit(1)

    try:
        with open(output_filename, mode='w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['first', 'last', 'house'])
            writer.writerows(rows)
    except IOError:
        print(f"Could not write to {output_filename}")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        if len(sys.argv) < 3:
            print("Too few command-line arguments")
        else:
            print("Too many command-line arguments")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    process_csv(input_filename, output_filename)

if __name__ == "__main__":
    main()
