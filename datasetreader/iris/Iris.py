class Iris:
    def __init__(self, row: list):
        self.sepal_length = float(row[0])
        self.sepal_width = float(row[1])
        self.petal_length = float(row[2])
        self.petal_width = float(row[3])
        self.class_name = row[4]
