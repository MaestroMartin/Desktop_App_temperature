import json 


class Registration:
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
        if len(entered_pasword) <= 6:
            print("You have short pasword!")
        elif entered_again_pasword <= 6:
            print("You have short pasword!")
            return entered_username 
        elif entered_password != entered_again_pasword:
            print("You have not same password!! ")
            return entered_username
        
    def verify(self, entered_username, entered_password):
        if entered_username == self.username:
            print("This username is allready used")
            return entered_username
        elif entered_password != self.password:
            print("Incorrect password")
        else:
            print("You are successfully logged in")
    

    def creating_new_acc(self, entered_again_pasword, entered_username, objekt):
        with open("ID.json","w") as file:
            a = {"username":entered_username, "pasword": entered_again_pasword}
            print(objekt["users"])
            objekt["users"].append(a)
            print(objekt["users"])
            json.dump(objekt, file, indent= 2 )

# Získání uživatelského jména a hesla od uživatele
entered_username = input("Write your username: ")
entered_password = input("Write your password: ")
entered_again_pasword = input("write your password again: ")
