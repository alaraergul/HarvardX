import csv
import sys


def longest_match(sequence, str_to_find):
    """
    This function returns the maximum number of times that an STR repeats in a DNA sequence.
    """
    max_repeats = 0
    current_repeats = 0
    str_length = len(str_to_find)

    i = 0
    while i < len(sequence):
        if sequence[i:i + str_length] == str_to_find:
            current_repeats += 1
            max_repeats = max(max_repeats, current_repeats)
            i += str_length
        else:
            current_repeats = 0
            i += 1

    return max_repeats


def main():
    if len(sys.argv) != 3:
        print("Usage: python dna.py <database.csv> <sequence.txt>")
        sys.exit(1)

    with open(sys.argv[1], newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        database = list(reader)

    with open(sys.argv[2], 'r') as sequence_file:
        dna_sequence = sequence_file.read()

    strs = list(database[0].keys())[1:]

    sequence_counts = {str_name: longest_match(dna_sequence, str_name) for str_name in strs}

    for person in database:
        name = person['name']
        counts = {str_name: int(person[str_name]) for str_name in strs}
        if counts == sequence_counts:
            print(name)
            sys.exit(0)

    print("No match")


if __name__ == "__main__":
    main()
