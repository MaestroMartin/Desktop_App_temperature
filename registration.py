import json


class Registration:
    def __init__(self, username, password, data):
        self.username = username
        self.password = password
        self.data = self.load()

    def load(self):
        try:
            with open("ID_big_project.json", "r") as file:
                data = json.load(file)
                return data["USERS"]
        except FileNotFoundError:
            print("JSON file not found.")
            return []
        except json.JSONDecodeError:
            print("Error decoding Json.")
            return []

    def first_part(self, entered_username):
        if len(entered_username) <= 6:
            print("You have a short username!")
            return entered_username

    def second_part(self, entered_password, entered_again_password):
        if len(entered_password) <= 6 or len(entered_again_password) <= 6:
            print("You have a short password!")
            return False
        return True

    def verify(self):
        for user in self.data:
            if user["username"] == self.username:
                print("This username is already used")
                return False
        if self.password != entered_password:
            print("Incorrect password")
            return False
        print("You are successfully logged in")
        return True

    def creating_new_acc(self, entered_again_password):
        with open("ID_big_project.json", "w") as file:
            self.data.append({"username": self.username, "password": entered_again_password})
            json.dump({"users": self.data}, file, indent=2)

# Získání uživatelského jména a hesla od uživatele
entered_username = input("Write your username: ")
entered_password = input("Write your password: ")
entered_again_password = input("Write your password again: ")

# Vytvoření instance registrace
reg = Registration(entered_username, entered_password, [])

# Zkontrolovat délku hesel
if not reg.second_part(entered_password, entered_again_password):
    print("Registration failed. Please enter a valid password.")
else:
    # Vytvořit nový účet
    reg.creating_new_acc(entered_again_password)
    print("Registration successful!")
