# Importing Cube and Pyramid classes from modules Lab5.Cube and Lab5.Pyramid
from Cube import Cube
from Pyramid import Pyramid

# Interface class for creating, drawing, and manipulating 3D shapes
class ShapeInterface:
    def __init__(self):
        self.shape = None

    # Method to create a cube based on user input
    def create_cube(self):
        size = int(input("Enter cube size (1 or 2): "))
        color = input("Enter cube color (RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE): ")
        symbol = input("Enter cube symbol: ")
        remove_shades = input("Remove shades? (True/False): ").lower() == 'true'
        self.shape = Cube(size, color, symbol, remove_shades)

    # Method to create a pyramid based on user input
    def create_pyramid(self):
        size = int(input("Enter pyramid size (1 or 2): "))
        color = input("Enter pyramid color (RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE): ")
        symbol = input("Enter pyramid symbol: ")
        remove_shades_pyramid = input("Remove shades in pyramid? (True/False): ").lower() == 'true'
        self.shape = Pyramid(size, color, symbol, remove_shades_pyramid)

    # Method to draw the 3D representation of the shape
    def draw_3D(self):
        if self.shape is not None:
            self.shape.draw_3D()
        else:
            print("Error: No shape created. Use create_cube() or create_pyramid() first.")

    # Method to draw the 2D representation of the shape
    def draw_2D(self):
        if self.shape is not None:
            self.shape.draw_2D()
        else:
            print("Error: No shape created. Use create_cube() or create_pyramid() first.")

    # Method to set a new size for the shape
    def set_size(self):
        if self.shape is not None:
            size = int(input("Enter new size (1 or 2): "))
            self.shape.set_size(size)
        else:
            print("Error: No shape created. Use create_cube() or create_pyramid() first.")

    # Method to save the 3D shape to a file
    def save_shape_3D(self):
        if self.shape is not None:
            filename = input("Enter the filename to save the 3D shape: ")
            if isinstance(self.shape, Cube):
                self.shape.saveCube_3D(filename + ".txt")
            elif isinstance(self.shape, Pyramid):
                self.shape.savePyramid_3D(filename + ".txt")
        else:
            print("Error: No shape created. Use create_cube() or create_pyramid() first.")

    # Method to display the 2D representation of the shape based on user input
    def display_2D_option(self):
        if self.shape is not None:
            option = input("Display 2D representation? (True/False): ").lower() == 'true'
            if option:
                self.shape.draw_2D()
        else:
            print("Error: No shape created. Use create_cube() or create_pyramid() first.")

# Example usage of the ShapeInterface
interface = ShapeInterface()

# User input to choose the type of shape (cube or pyramid)
shape_type = input("Enter shape type (cube-c/pyramid-p): ").lower()
if shape_type == 'c':
    interface.create_cube()
elif shape_type == 'p':
    interface.create_pyramid()
else:
    print("Invalid shape type. Choose 'cube' or 'pyramid'.")

# Displaying the 3D representation, saving to a file, and displaying the 2D representation
interface.draw_3D()
interface.save_shape_3D()
interface.display_2D_option()
