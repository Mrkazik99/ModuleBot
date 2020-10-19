import random


async def roll_dice():
    my_dict = {
        'Tetrahedron': '{"desc": "Tetrahedron", "text": "Tetrahedron: ' + str(
            random.randint(1, 4)) + '", "withImage": "False"}',
        'Cube': '{"desc": "Cube", "text": "Cube: ' + str(random.randint(1, 6)) + '", "withImage": "False"}',
        'Octahedron': '{"desc": "Octahedron", "text": "Octahedron: ' + str(
            random.randint(1, 8)) + '", "withImage": "False"}',
        'Pentagonal trapezohedron': '{"desc": "Pentagonal trapezohedron", "text": "Pentagonal trapezohedron: ' + str(
            random.randint(1, 10)) + '", "withImage": "False"}',
        'Dodecahedron': '{"desc": "Dodecahedron", "text": "Dodecahedron: ' + str(
            random.randint(1, 12)) + '", "withImage": "False"}',
        'Icosahedron': '{"desc": "Icosahedron", "text": "Icosahedron: ' + str(
            random.randint(1, 20)) + '", "withImage": "False"}'
    }
    return my_dict
