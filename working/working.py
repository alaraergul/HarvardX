import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)"
    match = re.match(pattern, s)

    if not match:
        raise ValueError("Invalid time format")

    start_hour, start_min, start_period, end_hour, end_min, end_period = match.groups()

    start_min = start_min if start_min else "00"
    end_min = end_min if end_min else "00"

    start_24 = to_24_hour_format(int(start_hour), int(start_min), start_period)
    end_24 = to_24_hour_format(int(end_hour), int(end_min), end_period)

    return f"{start_24} to {end_24}"

def to_24_hour_format(hour, minute, period):
    if not (0 <= minute < 60):
        raise ValueError("Invalid minute value")
    if not (1 <= hour <= 12):
        raise ValueError("Invalid hour value")

    if period == "AM":
        if hour == 12:
            hour = 0
    elif period == "PM":
        if hour != 12:
            hour += 12

    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()
