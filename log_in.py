import json


class User:
    def __init__(self, username, password, data):
        self.username = username
        self.password = password
        self.data = data

    def load(file_path):
        with open("ID2.json","r") as file:
            data = file.read()
            return data["users"]
    
    def first_part(self,entered_username):
        if len(entered_username) <= 6:
            print("you have short username!")
            return entered_username
    
    def second_part(self,entered_password,entered_username):
        if len(entered_password) <= 8:
            print("You have short pasword!")
            return entered_username

    def login(self, entered_username, entered_password):
        for users in self.data:
            if users['username'] == entered_username:
                if users['password'] == entered_password:
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

