"""
RoomArea
Author: Nathan Pastor

Original assignment by: Edhesive Intro to CS

Find the area of an irregularly shaped room with the shape as shown in room.png.

Ask the user to enter the values for sides A, B, C, D, and E and print out the total room area.

"""
import os
import importlib.util

def run_tests():
  """
  This function will check for the pytest module
  before calling it to run the included tests.py
  """
  if importlib.util.find_spec('pytest') is None: # Check if pytest is installed
    os.system('python3 -m pip install -q pytest')

  command = "python3 -m pytest --tb=line -v tests.py"
  print(command)
  os.system(command)

def right_triangle_area(base, height): 
  """
  Given the base and height of a right triangle, returns the area.

  Parameters: base(float) - base is the base of the triangle
  height(float) - height is the height of the triangle

  Returns:  base_x_height(float) - area of the triangle

  """
  base_x_height = float(base * height) / (2)

  return base_x_height


def rectangle_area(length, width):
  """
  Given the length and width of a rectangle, returns the area.

  Parameters: length(float) - length is the length of the rectangle
  width(float) - width is the width of the rectangle

  Returns: length_x_width(float) - area of the rectangles

  """
  length_x_width = float(length * width)
  return length_x_width


def room_area(a, b, c, d, e):
  """
  I broke it up as the smaller rectangle as rectangle1 and the bigger rectangle as rectangle2. I did the triangle as right_triangle.

  Parameters: a, b, c, d, e (floats) - These are all the different sides of the room.

  Returns: rectangle1+rectangle2+triangle(float) - the area of alls the shpes added together

  """
  rectangle1 = rectangle_area(d-b-e, a-c)
  rectangle2 = rectangle_area(a, b)
  triangle = right_triangle_area(a-c, e)
  return rectangle1+rectangle2+triangle



if __name__ == "__main__":
  os.system("clear") # clears the console each time you run
  
  a = float(input("A: "))
  b = float(input("B: "))
  c = float(input("C: "))
  d = float(input("D: "))
  e = float(input("E: "))


  final_area = room_area(a, b, c, d, e)
  print("Room area: " + str(final_area))

  tests = input("Run tests? (y/n)")
  if tests.lower() == 'y':
    run_tests()