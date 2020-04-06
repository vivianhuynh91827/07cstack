from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 0, 0 ]
edges = []
polygons = []
transform = new_matrix()
ident(transform)
csystems = [transform]

parse_file( 'script', edges, polygons, csystems, screen, color )
print("Image saved as robot.png")
