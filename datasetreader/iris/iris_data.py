import csv
import string

from datasetreader.iris.Iris import Iris


def get_iris(filename: string, delimiter: string):
    with open(filename) as iris_file:
        iris_reader = csv.reader(iris_file, delimiter=delimiter)
        iris_array = []
        for row in iris_reader:
            iris_array.append(Iris(row))
        return iris_array
