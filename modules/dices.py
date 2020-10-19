import random
import json


async def roll_dice():
    my_dict = {
        'Tetrahedron': 'Tetrahedron: ' + str(random.randint(1, 4)),
        'Cube': 'Cube: ' + str(random.randint(1, 6)),
        'Octahedron': 'Octahedron: ' + str(random.randint(1, 8)),
        'Pentagonal trapezohedron': 'Pentagonal trapezohedron: ' + str(random.randint(1, 10)),
        'Dodecahedron': 'Dodecahedron: ' + str(random.randint(1, 12)),
        'Icosahedron': 'Icosahedron: ' + str(random.randint(1, 20))
    }
    return my_dict
