"""
Unit and regression test for the geometry_analysis package.
"""

# Import package, test suite, and other packages as needed
import numpy as np
import itertools
import geometry_analysis
import pytest
import sys


@pytest.fixture()
def water_molecule():
    name = 'water'
    symbols = ['H', 'O', 'H']
    coordinates = np.array([[2, 0, 0], [0, 0, 0], [0, 0, 2]], dtype=np.float64)
    return geometry_analysis.molecule.Molecule(name, symbols, coordinates)


def test_geometry_analysis_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "geometry_analysis" in sys.modules


def test_calculate_distance():
    '''Test that pair distances are calculated correctly.'''
    r1 = np.array([0, 0, -1])
    r2 = np.array([0, 1, 0])
    expected_distance = np.sqrt(2.)
    calculated_distance = geometry_analysis.measure.calculate_distance(r1, r2)
    assert np.abs(expected_distance - calculated_distance) < 1e-6


# Create four random sets of points
np.random.seed(42)
points = [np.random.random((3, 3))
          for j in range(4)]


@pytest.mark.parametrize("points", points)
def test_calculate_angle(points):
    '''Test that pointss are cacluated correctly.

    Relies on the fact that all angles between three points is pi radians.'''
    expected_angle = 2 * np.pi
    calculated_angle = 0
    for permutation in itertools.permutations(points):
        calculated_angle += geometry_analysis.measure.calculate_angle(permutation[0],
                                                                      permutation[1],
                                                                      permutation[2])
    assert np.isclose(expected_angle, calculated_angle)


def test_molecule_bonds(water_molecule):
    '''Test that bonds are calculated correctly.'''
    num_bonds = len(water_molecule.bonds)
    assert num_bonds == 3


def test_molecule_coords_setter(water_molecule):
    '''Test that bond list is rebuilt when we reset coordinates.'''
    water_molecule.coordinates = water_molecule.coordinates * 100
    new_num_bonds = len(water_molecule.bonds)
    assert new_num_bonds == 0


def test_name_type_check():

    name = 24
    symbols = ['H', 'O', 'H']
    coordinates = np.array([[2, 0, 0], [0, 0, 0], [0, 0, 2]], dtype=np.float64)
    with pytest.raises(TypeError):
        water = geometry_analysis.molecule.Molecule(name, symbols, coordinates)
