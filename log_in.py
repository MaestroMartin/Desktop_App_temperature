import json


class Login:
    def __init__(self, username, password, data):
        self.username = username
        self.password = password
        self.data = data

    @staticmethod
    def load(file_path):
        with open("ID2.json","r") as file:
            data = file.read()
            objekt = json.loads(data)
            print(objekt)
    
    def first_part(self,entered_username):
        if len(entered_username) <= 6:
            print("you have short username!")
            return entered_username
    
    def second_part(self,entered_pasword,entered_username):
        if len(entered_pasword) <= 8:
            print("You have short pasword!")
            return entered_username

    def verify(self, entered_username, entered_password):
        if entered_username != self.username:
            print("Incorrect username")
        elif entered_password != self.password:
            print("Incorrect password")
        else:
            print("You are successfully logged in")

# Získání uživatelského jména a hesla od uživatele
entered_username = input("Write your username: ")
entered_password = input("Write your password: ")
