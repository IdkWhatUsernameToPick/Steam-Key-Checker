import sys
import requests

def is_valid_steam_key(key):
    # Simple validation to check if the key looks like a Steam key
    return len(key) == 17 and key.count('-') == 2

def check_steam_key(key):
    url = f"https://store.steampowered.com/account/ajaxregisterkey/?key={key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx errors
        data = response.json()
        if data.get("success") and data.get("purchase_receipt_info"):
            return False  # Key has been used
        else:
            return True  # Key is valid and unused
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False
    except requests.exceptions.JSONDecodeError:
        print("Error: Invalid response from the API.")
        return False

if __name__ == "__main__":
    while True:
        steam_key = input("Enter a Steam key to check (or 'exit' to quit): ")
        if steam_key.lower() == "exit":
            break

        if not is_valid_steam_key(steam_key):
            print("Invalid Steam key format. Please enter a valid key.")
            continue

        result = check_steam_key(steam_key)

        if result:
            print("The Steam key is valid and unused.")
        else:
            print("The Steam key has been used.")
