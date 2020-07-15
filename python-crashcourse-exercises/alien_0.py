class Alien:
    def __init__(self, speed = ''):
        self.speed = speed

    alien_0['speed'] = self.speed
    alien_0 = {'x_increment': 0, 'y_increment': 25, 'speed': ''}

    if alien_0['speed'] == 'slow':
        x_increment = 1
    elif alien_0['speed'] == 'medium':
        x_increment = 2
    elif alien_0['speed'] == 'fast':
        x_increment = 3
    else:
        raise AttributeError
    alien_0['x_position'] = alien_0['x_increment'] + x_increment

    print(f"New position: {alien_0['x_increment']}")
