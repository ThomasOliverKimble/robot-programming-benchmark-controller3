"""Simple robot controller."""

from controller import Robot
import sys

# Define the target motor position in radians.
target = 16

# Get pointer to the robot.
robot = Robot()

# Print the program output on the console
print("Moving the motors of the Thymio II to position " + str(target) + ".")

# Set the target position of the left and right wheels motors.
robot.getDevice("motor.left").setPosition(target)
robot.getDevice("motor.right").setPosition(target)
