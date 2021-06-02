class plates:
    def __init__(self, number, name, drawing_number, thickness, x, y, grade):
        self.number = number
        self.name = name
        self.drawing_number = drawing_number
        self.grade = grade
        self.weight = thickness * (x/1000) * (y/1000) * 7,85


