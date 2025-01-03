# 6.00.2x Problem Set 2: Simulating robots

import math
import random

import ps2_visualize
import pylab

import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"

import numpy as np

# a = np.array([0, 1, 2])
# print(a)
# print(type(a))

##################
## Comment/uncomment the relevant lines, depending on which version of Python you have
##################

# For Python 3.5:
# from ps2_verify_movement35 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.5 

# For Python 3.6:
from ps2_verify_movement310 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.6


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
           
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


class RectangularRoom:
    """
    A RectangularRoom represents a rectangular region containing clean or dirty tiles.
    """

    def __init__(self, height, width):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.

        height: an integer > 0
        width: an integer > 0
        """
        self.height = height
        self.width = width
        self.matrix = np.zeros((height, width), dtype=int)

    def cleanTileAtPosition(self, pos):
        """
        Marks the tile at the given position as cleaned.

        pos: a Position object
        """
        x, y = pos.getX(), pos.getY()
        if self.isPositionInRoom(pos):
            self.matrix[x][y] = 1

    def isTileCleaned(self, m, n):
        """
        Checks if the tile at (m, n) has been cleaned.

        m: an integer (row index)
        n: an integer (column index)
        returns: True if (m, n) is cleaned, False otherwise
        """
        return self.matrix[m][n] == 1

    def getNumTiles(self):
        """
        Returns the total number of tiles in the room.

        returns: an integer
        """
        return self.height * self.width

    def getNumCleanedTiles(self):
        """
        Returns the total number of cleaned tiles in the room.

        returns: an integer
        """
        return np.sum(self.matrix)

    def getRandomPosition(self):
        """
        Returns a random position inside the room.

        returns: a Position object
        """
        x = random.randint(0, self.height - 1)
        y = random.randint(0, self.width - 1)
        return Position(x, y)

    def isPositionInRoom(self, pos):
        """
        Checks if the given position is inside the room.

        pos: a Position object
        returns: True if the position is within the bounds of the room, False otherwise
        """
        x, y = pos.getX(), pos.getY()
        return 0 <= x < self.height and 0 <= y < self.width



# === Problem 2
class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """

    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        self.position = room.getRandomPosition()  # Start at a random position
        self.direction = random.uniform(0, 360)  # Random direction in degrees
        self.room.cleanTileAtPosition(self.position)  # Clean the starting tile

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position

    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.

        This method is meant to be overridden by subclasses to define a specific
        movement strategy.
        """
        raise NotImplementedError  # Abstract method to be implemented by subclasses



# === Problem 3
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # Calculate the new position based on current position, direction, and speed
        new_position = self.position.getNewPosition(self.direction, self.speed)
        
        # Check if the new position is within the room
        if self.room.isPositionInRoom(new_position):
            # Move to the new position
            self.setRobotPosition(new_position)
            # Clean the tile at the new position
            self.room.cleanTileAtPosition(new_position)
        else:
            # If the new position is outside the room, choose a new random direction
            self.setRobotDirection(random.uniform(0, 360))


# Uncomment this line to see your implementation of StandardRobot in action!
##testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 4
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials, robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    total_time_steps = 0  # To accumulate the total time steps across trials

    for trial in range(num_trials):
        # Create the room and the robots
        room = RectangularRoom(height, width)
        robots = [robot_type(room, speed) for _ in range(num_robots)]

        time_steps = 0
        while room.getNumCleanedTiles() / room.getNumTiles() < min_coverage:
            # Update all robots for one time step
            for robot in robots:
                robot.updatePositionAndClean()
            time_steps += 1

        # Add the time steps for this trial to the total
        total_time_steps += time_steps

    # Compute the mean time steps
    mean_time_steps = total_time_steps / num_trials
    return mean_time_steps

# Uncomment this line to see how much your simulation takes on average
##print(runSimulation(1, 1.0, 10, 10, 0.75, 30, StandardRobot))


# === Problem 5
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # Choose a new random direction between 0 and 360 degrees
        new_direction = random.uniform(0, 360)
        self.setRobotDirection(new_direction)
        
        # Calculate the new position based on the chosen direction
        new_position = self.position.getNewPosition(new_direction, self.speed)
        
        # Check if the new position is within the room
        if self.room.isPositionInRoom(new_position):
            # Move the robot to the new position and clean the tile
            self.setRobotPosition(new_position)
            self.room.cleanTileAtPosition(new_position)



def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print("Plotting", num_robots, "robots...")
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

    
def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300//width
        print("Plotting cleaning time for a room of width:", width, "by height:", height)
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()
    

# === Problem 6
# NOTE: If you are running the simulation, you will have to close it 
# before the plot will show up.

#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#

#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#
