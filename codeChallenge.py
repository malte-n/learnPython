class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = []
        for y in range(self.height):
            for x in range(self.width):
                self.cells.append((x, y))

        #iterates over the list and returns each object via yield more efficiently
        def __iter__(self):
            for cell in self.cells:
                yield cell


class TicTacToe(Board):
    def __init__(self):
        super().__init__(width=3, height=3)
