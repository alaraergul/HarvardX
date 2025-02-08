from datetime import date
import inflect
import sys

p = inflect.engine()

def main():
    birthdate_str = input("Date of birth (YYYY-MM-DD): ")
    try:
        birthdate = date.fromisoformat(birthdate_str)
    except ValueError:
        sys.exit("Invalid date format. Please enter date as YYYY-MM-DD.")

    minutes = calculate_minutes(birthdate)
    minutes_in_words = convert_to_words(minutes)

    print(f"{minutes_in_words.capitalize()} minutes")

def calculate_minutes(birthdate):
    today = date.today()
    delta = today - birthdate
    minutes = delta.days * 24 * 60
    return minutes

def convert_to_words(number):
    return p.number_to_words(number, andword="", zero="zero")

if __name__ == "__main__":
    main()
