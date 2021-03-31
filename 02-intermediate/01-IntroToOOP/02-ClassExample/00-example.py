class User:
    # method that executes when a object of this class is created
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # a method associated with the class
    def follow(self, user):
        user.followers += 1
        self.following += 1

    # method that represents the class objects as a string
    # this is what is going to be returned if print(object) is called
    def __str__(self):
        return f"username: {self.username}, followers: {self.followers}, following: {self.following}"


user_1 = User("001", "Davi")
user_2 = User("002", "John")
user_3 = User("003", "Emily")
user_4 = User("004", "Lara")

user_1.follow(user_4)
user_3.follow(user_4)
user_4.follow(user_1)
user_4.follow(user_3)
user_3.follow(user_2)


print(user_1)
print(user_2)
print(user_3)
print(user_4)
