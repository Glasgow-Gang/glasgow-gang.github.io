from controller import Robot
import math

# Initialize the robot
robot = Robot()

# Time step for the simulation (ms)
time_step = int(robot.getBasicTimeStep())

# Get left leg joints
hip_yaw_pitch = robot.getDevice('LHipYawPitch')
hip_roll = robot.getDevice('LHipRoll')
hip_pitch = robot.getDevice('LHipPitch')
knee_pitch = robot.getDevice('LKneePitch')
ankle_pitch = robot.getDevice('LAnklePitch')
ankle_roll = robot.getDevice('LAnkleRoll')

# Enable position control on the joints
hip_yaw_pitch.setPosition(0.0)
hip_roll.setPosition(0.0)
hip_pitch.setPosition(0.0)
knee_pitch.setPosition(0.0)
ankle_pitch.setPosition(0.0)
ankle_roll.setPosition(0.0)

# Simulation loop
t = 0.0  # Time variable for generating dynamic angles
while robot.step(time_step) != -1:
    # Update the time
    t += time_step / 1000.0  # Convert time step from ms to seconds

    # Define joint angles dynamically (e.g., using sine wave for smooth motion)
    q1 = math.sin(t) * 0.2   # Hip yaw oscillates between -0.2 and 0.2 radians
    q2 = math.sin(t) * 0.1   # Hip roll oscillates between -0.1 and 0.1 radians
    q3 = math.cos(t) * 0.5   # Hip pitch oscillates between -0.5 and 0.5 radians
    q4 = math.sin(t) * 0.785 # Knee pitch oscillates between -0.785 and 0.785 radians
    q5 = math.cos(t) * 0.5   # Ankle pitch oscillates between -0.5 and 0.5 radians
    q6 = math.sin(t) * 0.1   # Ankle roll oscillates between -0.1 and 0.1 radians

    # Set joint angles to the updated dynamic values
    hip_yaw_pitch.setPosition(q1)
    hip_roll.setPosition(q2)
    hip_pitch.setPosition(q3)
    knee_pitch.setPosition(q4)
    ankle_pitch.setPosition(q5)
    ankle_roll.setPosition(q6)

    # Wait for the next time step
    robot.step(time_step)
