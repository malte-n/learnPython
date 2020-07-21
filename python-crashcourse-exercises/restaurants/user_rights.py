from restaurant import Restaurant


class User:
    def __init__(self, first_name, last_name, middle_name=""):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        formatted_name = f"{self.first_name} {self.last_name}"
        return formatted_name

    def greet_user(self):
        print(
            f"\nWelcome, {self.first_name} {self.last_name}!\n"
            "Your table is right over here. Please follow me."
        )


class AdminPriviledges:
    def __init__(self, priviledges=""):
        self.priviledges = ["can add post", "can delete post", "can ban user"]

    def show_priviledges(self):
        for priviledge in self.priviledges:
            print(priviledge)


class Admin(User):
    def __init__(self, first_name, last_name, middle_name=""):
        super().__init__(first_name, last_name)
        self.priviledges = AdminPriviledges()


jan = User(first_name="Jan", last_name="Kowalski")
jan.describe_user()
jan.greet_user()

# jan.priviledges.show_priviledges()

restaurant = Restaurant("Stelzer", "German")
print(restaurant.cuisine_type)

test_user = User(first_name="Jan", last_name="Kowalski")
name_test_user = test_user.describe_user()
print(name_test_user)
