import sys

class Parser:
    'Parsing class. Allow to display usages, open a file and get all usefull informations of it'

    def __init__(self, argv):
        self.checkArgv(argv)
        self.filepath = argv[0]

    def openFile(self):
        try:
            fileObject = open(self.filepath, 'r')
        except IOError:
            print("This file does not exist. Try ./vacuumCleaner -h for usage", file=sys.stderr)
            sys.exit(84)
        self.fileData = fileObject.read().split('\n')
        fileObject.close()

    def checkArgv(self, argv):
        if len(argv) != 1:
            print("Wrong number of arguments. Try ./vacuumCleaner -h for usage", file=sys.stderr)
            sys.exit(84)
        if argv[0] == "-h" or argv[0] == "--help":
            self.displayUsage()

    def displayUsage(self):
        print("USAGE:\t./vacuumCleaner file")
        print("\tfile\tfile describing room and vacuum cleaner informations:")
        print("\t\tx y -> room dimension")
        print("\t\tx y o -> vacuum cleaner position and orientation ('o' must be one of the following character: 'N', 'E', 'S' or 'W')")
        print("\t\ti1i2...in -> vacuum cleaner instructions (must be one of the following instruction: 'G' for left, 'D' for right or 'A' for forward)")
        sys.exit(0)

    def isInteger(self, value):
        try: 
            int(value)
            return True
        except ValueError:
            return False

    def checkRoomDimensions(self, line):
        lineValues = line.split(' ')
        if len(lineValues) != 2:
            print("Room must have 2 dimensions x and y. Try ./vacuumCleaner -h for usage")
            sys.exit(84)
        for value in lineValues:
            if self.isInteger(value) == False:
                print("Room dimensions must be integers. Try ./vacuumCleaner -h for usage")
                sys.exit(84)
            if int(value) <= 0:
                print("Room dimensions must be strictly greater than 0. Try ./vacuumCleaner -h for usage")
                sys.exit(84)
        return tuple(int(i) for i in lineValues)

    def checkVacuumCleanerInformations(self, line, roomDimensions):
        lineValues = line.split(' ')
        if len(lineValues) != 3:
            print("Vacuum cleaner must have 2 positions x and y and 1 orientation. Try ./vacuumCleaner -h for usage")
            sys.exit(84)
        for index, value in enumerate(lineValues[:-1]):
            if self.isInteger(value) == False:
                print("Vacuum cleaner position must be integers. Try ./vacuumCleaner -h for usage")
                sys.exit(84)
            if int(value) < 0 or int(value) >= roomDimensions[index]:
                print("Vacuum cleaner position must be equal or greater than 0 and strictly inferior than room's dimension. Try ./vacuumCleaner -h for usage")
                sys.exit(84)
        if not lineValues[-1] in ['N', 'E', 'S', 'W']:
            print("Vacuum cleaner orientation must be one of the following character: 'N', 'E', 'S' or 'W'. Try ./vacuumCleaner -h for usage")
            sys.exit(84)
        return (tuple(int(i) for i in lineValues[:-1]), lineValues[-1])

    def checkVacuumCleanerInstructions(self, line):
        lineValues = [c for c in line]
        for value in lineValues:
            if not value in ['G', 'D', 'A']:
                print("Vacuum cleaner instruction must be one of the following instruction: 'G' for left, 'D' for right or 'A' for forward. Try ./vacuumCleaner -h for usage")
                sys.exit(84)
        return lineValues

    def parseFile(self):
        if len(self.fileData) != 3:
            print("File must have 3 lines of informations. Try ./vacuumCleaner -h for usage")
            sys.exit(84)

        roomDimensions = self.checkRoomDimensions(self.fileData[0])
        vacuumInformations = self.checkVacuumCleanerInformations(self.fileData[1], roomDimensions)
        vacuumInstructions = self.checkVacuumCleanerInstructions(self.fileData[2])
        return (roomDimensions, vacuumInformations, vacuumInstructions)