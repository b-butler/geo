"""
Unit and regression test for the geometry_analysis package.
"""

# Import package, test suite, and other packages as needed
import numpy as np
import itertools
import geometry_analysis
import pytest
import sys


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


def test_calculate_angle():
    '''Test that pointss are cacluated correctly.'''
    points = np.array([[0, 0, 1],
                       [0, 0, 0],
                       [1, 0, 0]])
    expected_angle = np.pi
    calculated_angle = 0
    for permutation in itertools.permutations(points):
        calculated_angle += geometry_analysis.measure.calculate_angle(permutation[0],
                                                                      permutation[1],
                                                                      permutation[2])
    assert np.abs(expected_angle - calculated_angle) < 1e-6
