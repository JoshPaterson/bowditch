from numpy import array, interp

refraction_reed_table = array([14, 15, 17, 19, 21, 24, 27, 30, 35, 40, 45, 50, 55, 60, 65, 75, 80, 85, 90],
                          [3.8, 3.4, 3.1, 2.8, 2.5, 2.2, 1.9, 1.7, 1.4, 1.2, 1.0, .8, .7, .6, .5, .4, .3, .2, .1])

def refraction_reed(altitude):
    if