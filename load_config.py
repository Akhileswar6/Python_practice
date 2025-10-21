import yaml

# Load YAML config
with open("config.yml", "r") as file:
    config = yaml.safe_load(file)

# Example: display user info
user = config["user"]
print(f"Hello, {user['name']}!")
print(f"GitHub: {user['github']}")
print(f"LinkedIn: {user['linkedin']}")

# Example: check active folders
folders = config["folders"]
for folder, active in folders.items():
    status = "active" if active else "inactive"
    print(f"{folder} folder is {status}")

# Example: conditional message
if config["python"]["show_welcome_message"]:
    print("\nWelcome to Python Practice Repository!\n")
