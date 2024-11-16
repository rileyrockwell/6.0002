from ps2 import *

position = Position(1, 1)
room = RectangularRoom(2, 2)
print(room.cleanTileAtPosition(position))
print(room.cleanTileAtPosition(Position(0, 0)))
print(room.matrix)
print(room.height)
print(room.width)
print(room.getNumCleanedTiles())