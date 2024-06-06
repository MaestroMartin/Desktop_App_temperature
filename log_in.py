import json 

class Login:
  with open("ID2.json","r") as file:
    data = file.read()
    objekt = json.loads(data)
    print(objekt)
  
  def __init__(self, username, pasword):
    self.name = username
    self.pasword = password 

  def name(self, username, password):
    if username in data:
      print("You have correct username")
    elif len(username) <= 6:
      print("you have short username")

  username = input("Enter your username:\n")
  password = input("Enter your password:\n")
  def pasword(self, username, password):
    if password not in username:
      return username 
    elif len(password) <= 6:
      print("you have shor 
    else:
      print("you are succesfull loged")
  
