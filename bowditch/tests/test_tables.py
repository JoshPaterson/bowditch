from bowditch.data import tables
from numpy import isclose

data_arrays = [tables.refraction_data, tables.dip_data]

def test_table_size():
    for table in data_arrays:
        assert len(table[0]) == len(table[1])

def test_refraction_table():
    assert isclose(tables.refraction_table(35), 1.4)
    assert isclose(tables.refraction_table(31), 1.7)
    assert isclose(tables.refraction_table(57.5, interpolate=True), .65)
