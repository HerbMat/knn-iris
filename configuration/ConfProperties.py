import configparser

from datasetreader.iris.distance.IncludeAttributesConf import IncludeAttributesConf


class ConfProperties(object):
    def __init__(self):
        self.__config_properties = configparser.RawConfigParser()
        self.__config_properties.read('ai.properties')

    def get_neighbours(self) -> int:
        return int(self.__config_properties['knn']['neighbours'])

    def get_parts(self) -> str:
        return self.__config_properties['knn']['parts']

    def get_learn_file_name(self) -> str:
        return self.__config_properties['knn']['learnFile']

    def get_test_file_name(self) -> str:
        return self.__config_properties['knn']['testFile']

    def get_result_file_name(self) -> str:
        return self.__config_properties['knn']['resultFile']

    def get_delimiter(self) -> str:
        return self.__config_properties['knn']['delimiter']

    def get_include_attributes_conf(self) -> IncludeAttributesConf:
        return IncludeAttributesConf(
            self.__config_properties['knn']['includeSepalLength'] == 'true',
            self.__config_properties['knn']['includeSepalWidth'] == 'true',
            self.__config_properties['knn']['includePetalLength'] == 'true',
            self.__config_properties['knn']['includePetalWidth'] == 'true'
        )


conf_properties = ConfProperties()
