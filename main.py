from binance.client import Client

def main():
    # Read in the secrets
    with open("secrets.txt", "r") as f:
        BINANCE_API_KEY = f.readline().strip()
        BINANCE_API_SECRET = f.readline().strip()

    # Print secrets to make sure we read them correctly
    print(f"Key: {BINANCE_API_KEY}\nSecret: {BINANCE_API_SECRET}")

    # Create a client for interacting with the API
    client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)

    # Example call
    exchange_info = client.get_exchange_info()
    print(exchange_info)

    # NOTE: the above call runs even if you put in a fake key and secret,
    # so make sure your key and secret are right, or nothing will work!

    # Good luck :)

if __name__ == "__main__":
    main()