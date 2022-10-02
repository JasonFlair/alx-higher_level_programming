from models.rectangle import Rectangle

class Square(Rectangle):
    """for a square"""


    def __init__(self, size, x=0, y=0, id=None):
        """ initialiser """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates attributes of the rectangle"""
        count = 0
        for k, v in kwargs.items():
            if k == "id":
                self.id = kwargs['id']
            elif k == "size":
                self.size = kwargs['size']
            elif k == "x":
                self.x = kwargs['x']
            elif k == "y":
                self.y = kwargs['y']
        for arg in args:
            count += 1
        if count == 1:
            self.id = args[0]
        elif count == 2:
            self.id = args[0]
            self.size = args[1]
        elif count == 3:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
        elif count == 4:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]

    def to_dictionary(self):
        """returns dictionary representation"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    def __str__(self):
        """str representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

