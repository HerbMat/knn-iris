from datasetreader.iris import Iris
from datasetreader.iris.distance import EuclidisianDistanceMeter


class IrisKnn:
    def __init__(self, number_of_neighbours: int, elements: list, euclidisian_distance_meter: EuclidisianDistanceMeter):
        self.__number_of_neighbours = number_of_neighbours
        self.__elements = elements
        self.__euclidisian_distance_meter = euclidisian_distance_meter

    def find_class(self, iris: Iris):
        distances = []
        for iris_to_compare in self.__elements:
            distance = self.__euclidisian_distance_meter.calculate(iris_to_compare, iris)
            distances.append((iris_to_compare.class_name, distance))
        distances.sort(key=lambda x: x[1])
        neighbours = distances[: self.__number_of_neighbours]
        classes = {}
        for neighbour in neighbours:
            if neighbour[0] not in classes:
                classes[neighbour[0]] = 0
            classes[neighbour[0]] += 1
        return sorted(classes.items(), key=lambda item: item[1], reverse=True)[0]
