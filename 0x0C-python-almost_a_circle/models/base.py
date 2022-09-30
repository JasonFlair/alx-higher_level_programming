class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialiser"""
        self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def id(self):
        """returns id if id is not None"""
        return self.id
