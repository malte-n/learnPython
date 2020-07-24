from random import choice


class Randomwalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        # run as long as the list hasn't reached the defined num_points
        while len(self.x_values) < self.num_points:
            """Calculate all the points on the walk"""

            # calculate the x steps
            x_direction = choice([-1, 1])
            x_distance = choice([0, 1, 2, 3, 4, 5])
            x_step = x_direction * x_distance

            # calculate the y steps
            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4, 5])
            y_step = y_direction * y_direction

            # if both steps are 0, nothing moves and it shouldn't be appended to the list
            if x_step == 0 and y_step == 0:
                continue

            # calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

        print(f"This is x_values: {self.x_values}")
        print(f"This is y_values: {self.y_values}")
