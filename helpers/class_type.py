class ClassType():
    def __init__(self):
        self.id = id(ClassType)

    def set_class(self, class_type):
        self.id = id(class_type)

    def is_class(self, class_type):
        return id(class_type) == self.id