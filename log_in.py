import json 

class Login:
  with open("ID2.json","r") as file:
    data = file.read()
    objekt = json.loads(data)
    print(objekt)
  
  def __init__(self, username, pasword):
    self.name = username
    self.pasword = password 

  def name(self):
    if username in data:
      print("You have correct username")
    elif len(username) <= 6:
      print("you have short username")

  username = input("Enter your username:\n")

  def pasword(self):
    if password not in username:
      return username 
    else:
      print("you are succesfull loged")
  
