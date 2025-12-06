class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password   

    def validate_login(self, username, password):
        if self.username == username and self.__password == password:
            return "Login successful!"
        else:
            return "Invalid username or password."


user1 = User("kv", "1234")

u = input("Enter username: ")
p = input("Enter password: ")

print(user1.validate_login(u, p))
