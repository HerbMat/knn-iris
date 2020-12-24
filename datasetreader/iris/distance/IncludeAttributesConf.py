class IncludeAttributesConf:
    def __init__(self,
                 include_sepal_length: bool,
                 include_sepal_width: bool,
                 include_petal_length: bool,
                 include_petal_width: bool):
        self.include_sepal_length = include_sepal_length
        self.include_sepal_width = include_sepal_width
        self.include_petal_length = include_petal_length
        self.include_petal_width = include_petal_width
