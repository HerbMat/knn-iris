from math import sqrt

from datasetreader.iris import Iris
from datasetreader.iris.distance import IncludeAttributesConf


class EuclidisianDistanceMeter:
    def __init__(self, includes: IncludeAttributesConf):
        self.__includes = includes

    def calculate(self, first_iris: Iris, second_iris: Iris):
        distance = self.calculate_attribute(
            self.__includes.include_petal_length, first_iris.petal_length, second_iris.petal_length)
        distance = distance + self.calculate_attribute(
            self.__includes.include_petal_width, first_iris.petal_width, second_iris.petal_width)
        distance = distance + self.calculate_attribute(
            self.__includes.include_sepal_length, first_iris.sepal_length, second_iris.sepal_length)
        distance = distance + self.calculate_attribute(
            self.__includes.include_sepal_width, first_iris.sepal_width, second_iris.sepal_width)

        return sqrt(distance)

    @staticmethod
    def calculate_attribute(is_included: bool, first_value: int, second_value: int):
        if is_included:
            return (first_value - second_value) ** 2
        return 0
