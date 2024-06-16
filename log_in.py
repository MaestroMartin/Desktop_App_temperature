import json

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.data = self.load()

    def load(self):
        try:
            with open("ID_big_project.json", "r") as file:
                data = json.load(file)
                return data["users"]
        except FileNotFoundError:
            print("JSON file not found.")
            return []
        except json.JSONDecodeError:
            print("Error decoding JSON.")
            return []

    def first_part(self, entered_username):
        if len(entered_username) <= 6:
            print("You have a short username!")
            return entered_username
    
    def second_part(self, entered_password, entered_username):
        if len(entered_password) <= 8:
            print("You have a short password!")
            return entered_username

    def login(self, entered_username, entered_password):
        for user in self.data:
            if user['username'] == entered_username:
                if user['password'] == entered_password:
                    print("You are successfully logged in")
                    return True
                else:
                    print("Incorrect password")
                    return False
        print("Incorrect username")
        return False

# Získání uživatelského jména a hesla od uživatele
entered_username = input("Write your username: ")
entered_password = input("Write your password: ")

# Vytvoření instance uživatele a přihlášení
user = User(entered_username, entered_password)
user.login(entered_username, entered_password)
