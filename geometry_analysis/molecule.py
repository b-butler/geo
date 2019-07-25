"""
molecule.py
A python package for the MolSSI Software Summer School.

Handles the primary functions
"""
import numpy as np
import geometry_analysis as ga


class new_property(property):
    def __init__(self, fget=None, fset=None, fdel=None, fsetitem=None):
        super().__init__(fget, fset, fdel)
        self.fsetitem = fsetitem

    def setitem(self, fsetitem):
        return type(self)(self.fget, self.fset, self.fdel, fsetitem)

    def __setitem__(self, index, value):
        if self.fsetitem is None:
            raise AttributeError("Can't set item.")
        self.fsetitem(index, value)


class Molecule:
    def __init__(self, name, symbols, coordinates):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name is not a string.")

        self.symbols = symbols
        self._coordinates = coordinates
        self.bonds = self.build_bond_list()

    @property
    def num_atoms(self):
        return len(self.coordinates)

    @new_property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, new_coordinates):
        self._coordinates = new_coordinates
        self.bonds = self.build_bond_list()

    @coordinates.setitem
    def coordinates(self, index, value):
        self._coordinates[index] = value
        self.bonds = self.build_bond_list()

    def build_bond_list(self, max_bond=2.93, min_bond=0):
        """
        Build a list of bonds based on a distance criteria.
        Atoms within a specified distance of one another will be considered bonded.
        Parameters
        ----------
        max_bond : float, optional
        min_bond : float, optional
        Returns
        -------
        bond_list : list
            List of bonded atoms. Returned as list of tuples where the values are the atom indices.
        """

        bonds = {}

        for atom1 in range(self.num_atoms):
            for atom2 in range(atom1, self.num_atoms):
                distance = ga.calculate_distance(self.coordinates[atom1],
                                                 self.coordinates[atom2])

                if distance > min_bond and distance < max_bond:
                    bonds[(atom1, atom2)] = distance

        return bonds


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    random_coords = np.random.random([3, 3])
    name = 'my_mol'
    symbols = ['H', 'O', 'H']
    my_molecule = Molecule(name, symbols, random_coords)
    print('The coords are {}'.format(my_molecule.coordinates))
    my_molecule.coordinates[0] += 100.
    print('The coords are {}'.format(my_molecule.coordinates))
