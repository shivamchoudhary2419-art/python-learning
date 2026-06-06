import requests

username = input("Enter Github Username:")
response = requests.get(
    f"https://api.github.com/users/{username}"
)

print("Status Code:", response.status_code)


data = response.json()
if response.status_code == 200:
    print("User found")
    print("\n===== GitHub Profile =====")
    print("Username:", data["login"])
    print("Followers:", data["followers"])
    print("Following:", data["following"])
    print("Public Repos:", data["public_repos"])
    print("Profile URL:", data["html_url"])
    print("Account Type:", data["type"])
    print("Bio:", data["bio"])
    print("Created At:", data["created_at"])

else:
    print("User not found.")