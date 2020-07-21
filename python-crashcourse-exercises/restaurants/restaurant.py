class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(
            f"The new restaurant {self.restaurant_name} serves you {self.cuisine_type} food."
        )

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now officially open.")

    def set_number_served(self, number_guests_served):
        if number_guests_served >= self.number_served:
            self.number_served = number_guests_served
        else:
            print(f"The number of guests can't be less than 0.")

    def increment_number_served(self, added_number_served):
        self.number_served += added_number_served
        print(f"The number of customers served is now {self.number_served}.")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Chocolate", "Strawberry", "Vanilla"]

    def list_flavors(self):
        for flavor in self.flavors:
            print(flavor)


restaurant = IceCreamStand("Farmers", "american")

restaurant.open_restaurant()
restaurant.set_number_served(5)
print(restaurant.number_served)
restaurant.increment_number_served(2)

restaurant.list_flavors()
