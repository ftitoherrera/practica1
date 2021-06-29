"""my_controller__ controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, DistanceSensor, Motor

# create the Robot instance.

MAX_SPEED = 6.28



robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())
# ground sensors
gs = []
gsNames = ['gs1', 'gs2', 'gs3']

for i in range(3):
    gs.append(robot.getDistanceSensor(gsNames[i]))
    gs[i].enable(timestep)
    
leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    gsValues = []
    for i in range(3):
        gsValues.append(gs[i].getValue())
        
    leftSpeed  = 0.5*MAX_SPEED
    rightSpeed = 0.5*MAX_SPEED

    # Process sensor data here.
    # Process sensor data
    line_right = gsValues[0] > 600
    line_left = gsValues[2] > 600

    if line_right:
        leftSpeed=0.0
        rightSpeed=0.0
    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    leftMotor.setVelocity(leftSpeed)
    rightMotor.setVelocity(rightSpeed)

    pass

# Enter here exit cleanup code.
