# Crypto Converter using CoinGecko API

import requests

def get_crypto_price(base_currency, target_currency):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={base_currency}&vs_currencies={target_currency}"
    response = requests.get(url)
    data = response.json()
    return data.get(base_currency, {}).get(target_currency, 'Not Available')

def main():
    base_currency = input("Enter the cryptocurrency (e.g., bitcoin): ").lower()
    target_currency = input("Enter the target currency (e.g., usd): ").lower()
    price = get_crypto_price(base_currency, target_currency)
    print(f"1 {base_currency} = {price} {target_currency}")

if __name__ == "__main__":
    main()
