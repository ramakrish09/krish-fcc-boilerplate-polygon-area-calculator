class Rectangle:
  width = 0
  height = 0

  def __init__(self, width, height):
    self.width = width
    self.height = height 

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height;

  def get_area(self):
    return (self.width * self.height)

  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def __str__(self):
    return ("Rectangle(width=%s, height=%s)" % (self.width, self.height))

  def get_picture(self):
    string = ""
    if self.height > 50 or self.width > 50:
      string = "Too big for picture."
      return string

    for i in range(self.height):
      string += "*" * self.width + "\n"

    return string

  def get_amount_inside(self, obj):
    amount = int((self.width * self.height)/(obj.width * obj.height))
    return amount


class Square(Rectangle):
  side = 0

  def __init__(self, side):
    self.side = side
  # invoking the constructor of 
                # the parent class  
    Rectangle.__init__(self, side, side)

  def set_width(self, side):
    self.width = side
    self.side = side

  def set_height(self, side):
    self.height = side
    self.side = side

  def set_side(self, side):
    self.side = side

  def get_area(self):
    return (self.side * self.side)

  def get_perimeter(self):
    return (4 * self.side)

  def get_diagonal(self):
    return ((2 ** .5) * self.side)

  def __str__(self):
    return ("Square(side=%s)" % (self.side))

  def get_picture(self):
    string = ""
    if self.side > 50:
      string = "Too big for picture."

    for i in range(self.side):
      string += "*" * self.side + "\n"

    return string
