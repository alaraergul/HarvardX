import sys
import requests

def main():
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        price_usd = data['bpi']['USD']['rate_float']
    except requests.RequestException:
        print("Error fetching Bitcoin price")
        sys.exit(1)

    cost = bitcoins * price_usd

    print(f"${cost:,.4f}")

if __name__ == "__main__":
    main()
