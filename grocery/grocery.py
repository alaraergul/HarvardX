def main():
    from collections import Counter
    items = []

    try:
        while True:
            item = input().strip()
            items.append(item.lower())

    except EOFError:
        pass

    item_counts = Counter(items)

    sorted_items = sorted(item_counts.keys())
    for item in sorted_items:
        print(f"{item_counts[item]} {item.upper()}")

if __name__ == "__main__":
    main()
