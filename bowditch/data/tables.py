from numpy import array, searchsorted, interp
import math

def find_nearest(array,value):
    """ Finds the index of the value in a sorted `array` that most closely matches `value`

    see https://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array
    """
    idx = searchsorted(array, value, side="left")
    if idx > 0 and (idx == len(array) or math.fabs(value - array[idx-1]) < math.fabs(value - array[idx])):
        return idx-1
    else:
        return idx

refraction_data = array([[14, 15, 17, 19, 21, 24, 27, 30, 35, 40, 45, 50, 55, 60, 65, 75, 80, 85, 90],
                         [3.8, 3.4, 3.1, 2.8, 2.5, 2.2, 1.9, 1.7, 1.4, 1.2, 1.0, .8, .7, .6, .5, .4, .3, .2, .1]])

def refraction_table(alt, interpolate=False):
    if alt < 14:
        raise ValueError('Altitude is too low for this table')
    if not interpolate:
        return refraction_data[1, find_nearest(refraction_data[0], alt)]
    else:
        return round(interp(alt, refraction_data[0], refraction_data[1], right=0), 1)

def simple_refraction_table(alt):
    if alt < 14:
        raise ValueError('Altitude is too low for this table')
    if alt > 60:
        return 0
    elif alt >= 33:
        return 1
    else:
        return refraction_data[1, find_nearest(refraction_data[0], alt)]


dip_data = array([[1, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 100, 120, 140, 160, 180, 200, 220, 240],
                  [1, 2.2, 3.1, 3.8, 4.3, 4.9, 5.3, 6.1, 6.9, 7.5, 8.1, 8.7, 9.7, 10.6, 11.5, 12.3, 13.0, 13.7, 14.4, 15.0]])

def dip_table(height_ft, interpolate=False):
    if height_ft > 240:
        raise ValueError('Height too high for this table')
    if not interpolate:
        return dip_data[1, find_nearest(dip_data[0], height_ft)]
    else:
        return round(interp(height_ft, dip_data[0], dip_data[1], left=0), 1)