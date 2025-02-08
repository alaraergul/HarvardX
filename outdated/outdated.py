def main():
    import re
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        date_input = input("Date: ").strip()
        match1 = re.match(r'^(\d{1,2})/(\d{1,2})/(\d{4})$', date_input)
        if match1:
            month, day, year = map(int, match1.groups())
            if 1 <= month <= 12 and 1 <= day <= 31: 
                print(f"{year:04}-{month:02}-{day:02}")
                return
        match2 = re.match(r'^([A-Za-z]+) (\d{1,2}), (\d{4})$', date_input)
        if match2:
            month_name, day, year = match2.groups()
            if month_name in months:
                month = months.index(month_name) + 1
                day = int(day)
                if 1 <= day <= 31:
                    print(f"{year}-{month:02}-{day:02}")
                    return

        print("Invalid date format. Please try again.")

if __name__ == "__main__":
    main()
