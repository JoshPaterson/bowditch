from bowditch.data import tables
from numpy import isclose
from pytest import raises

data_arrays = [tables.refraction_data, tables.dip_data]

def test_table_size():
    for table in data_arrays:
        assert len(table[0]) == len(table[1])

def test_refraction_table():
    assert isclose(tables.refraction_table(35), 1.4)
    assert isclose(tables.refraction_table(31), 1.7)
    assert isclose(tables.refraction_table(37, interpolate=True), 1.3)
    with raises(ValueError):
        tables.refraction_table(10)

def test_simple_refraction_table():
    assert isclose(tables.simple_refraction_table(61), 0)
    assert isclose(tables.simple_refraction_table(35), 1)
    assert isclose(tables.simple_refraction_table(31), 1.7)
    with raises(ValueError):
        tables.simple_refraction_table(10)

def test_dip_table():
    assert isclose(tables.dip_table(20), 4.3)
    assert isclose(tables.dip_table(74), 8.1)
    assert isclose(tables.dip_table(90, interpolate=True), 9.2)
    with raises(ValueError):
        tables.dip_table(250)
