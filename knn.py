from configuration.ConfProperties import conf_properties

from datasetreader.iris.algorithm.IrisKnn import IrisKnn
from datasetreader.iris.distance.EuclidisianDistanceMeter import EuclidisianDistanceMeter
from datasetreader.iris.iris_data import get_iris

if __name__ == '__main__':
    neighbours = conf_properties.get_neighbours()
    iris_array = get_iris(conf_properties.get_learn_file_name(), conf_properties.get_delimiter())
    check_array = get_iris(conf_properties.get_test_file_name(), conf_properties.get_delimiter())
    euclidisian_distance_meter = EuclidisianDistanceMeter(conf_properties.get_include_attributes_conf())
    irisKnn = IrisKnn(neighbours, iris_array, euclidisian_distance_meter)
    with open(conf_properties.get_result_file_name(), 'w') as result_file:
        for iris in check_array:
            result_file.write('{},{},{},{},{}\n'.format(
                iris.sepal_length,
                iris.sepal_width,
                iris.petal_length,
                iris.petal_width,
                irisKnn.find_class(iris)[0]
            ))

    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')

    # x = list(map(lambda iris_element: iris_element.sepal_length, filter(lambda iris: iris.class_name == 'Iris-versicolor', iris_array)))
    # y = list(map(lambda iris_element: iris_element.sepal_width, filter(lambda iris: iris.class_name == 'Iris-versicolor', iris_array)))
    # z = list(map(lambda iris_element: iris_element.petal_length, filter(lambda iris: iris.class_name == 'Iris-versicolor', iris_array)))
    # c = list(map(lambda iris_element: iris_element.petal_width, filter(lambda iris: iris.class_name == 'Iris-versicolor', iris_array)))

    # img = ax.scatter(x, y, z, c=c, cmap=plt.hot())
    # img = ax.scatter(x, y, z, color='b')
    # fig.colorbar(img)
    # plt.show()
