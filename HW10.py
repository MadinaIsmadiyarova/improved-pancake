class Room:
    def __init__(self, walls, floor, window, door):
        self.walls = walls
        self.floor = floor
        self.window = window
        self.door = door


class Livingroom(Room):
    def __init__(self, walls, floor, window, door, sofa):
        super().__init__(walls, floor, window, door)
        self.sofa = sofa

    def relax(self):
        print('To have a rest')


class Bedroom(Living_room):
    def __init__(self, walls, floor, window, door, sofa, bed):
        super().__init__(walls, floor, window, door, sofa)
        self.bed = bed

    def sleep(self):
        print('To sleep')


