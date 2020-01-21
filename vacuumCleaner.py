import sys
import math

class VacuumCleaner:
    'VacuumCleaner class. It can turn on itself or move forward following instrcutions'

    ORIENTATIONS = ['N', 'E', 'S', 'W']

    def __init__(self, position, orientation, room):
        self.position = position
        self.turnOffset = self.ORIENTATIONS.index(orientation)
        self.room = room

    def readInstructions(self, instructions):
        for instruction in instructions:
            if instruction == 'A':
                self.forward()
            else:
                self.turn(instruction)

    def turn(self, direction):
        if direction == 'G':
            self.turnOffset -= 1
        else:
            self.turnOffset += 1

    def forward(self):
        orientationOffset = math.pi / 2 * self.turnOffset
        self.position = (
            self.position[0] + round(math.sin(orientationOffset)),
            self.position[1] + round(math.cos(orientationOffset))
        )
        if self.checkPosition() == False:
            print("Vacuum cleaner is out of the room.", file=sys.stderr)
            sys.exit(84)

    def checkPosition(self):
        if 0 <= self.position[0] < self.room.dimension[0] and \
            0 <= self.position[1] < self.room.dimension[1]:
            return True
        return False

    def displayVacuumCleanerInformations(self):
        orientation = self.ORIENTATIONS[self.turnOffset % 4]
        print(self.position[0], self.position[1], orientation)