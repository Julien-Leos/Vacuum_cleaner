import sys
from vacuumCleaner import VacuumCleaner

class Room:
    'Room class. Allow to add new vacuum cleaners to it.'

    def __init__(self, dimension):
        self.dimension = dimension
        self.vacuumsCleaner = []

    def addVacuumCleaner(self, position, orientation):
        newVacuumCleaner = VacuumCleaner(position, orientation, self)
        self.vacuumsCleaner.append(newVacuumCleaner)
        return newVacuumCleaner