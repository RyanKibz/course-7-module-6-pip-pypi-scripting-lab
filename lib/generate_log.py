from datetime import datetime
import requests


def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            print("Data fetched successfully.")
            return response.json()

        print("Failed to fetch data.")
        return {}

    except requests.RequestException:
        print("An error occurred while fetching data.")
        return {}


def write_log(post):
    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported",
        f"Fetched Post Title: {post.get('title', 'No title found')}"
    ]

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"log_{timestamp}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")


if __name__ == "__main__":
    post = fetch_data()

    print(
        "Fetched Post Title:",
        post.get("title", "No title found")
    )

    write_log(post)