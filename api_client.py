import requests


def fetch_and_display_users(num_users):
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Error: HTTP {response.status_code}")
            return None

        users = response.json()

        for user in users[:num_users]:
            print(f"Name : {user['name']}")
            print(f"Email: {user['email']}")
            print(f"City : {user['address']['city']}")
            print("-" * 30)

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None

    except (KeyError, ValueError, TypeError):
        print("Unexpected data received from the API.")
        return None


# Example calls
fetch_and_display_users(3)