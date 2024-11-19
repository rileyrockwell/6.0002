from ps2 import *

position1 = Position(0, 0)
position2 = Position(1, 1)
room = RectangularRoom(2, 2)
print(room.isPositionInRoom(Position(0, 0)))
print(room.isPositionInRoom(Position(-0.10, 0.00)))