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

# Set target foot position (in meters)
x_target = 0.05  # Target forward position (x)
y_target = 0.0  # Target lateral position (y)
z_target = -0.35  # Target height (z)

# Leg lengths (meters)
L_thigh = 0.1  # Length of the upper leg (hip to knee)
L_shin = 0.1029  # Length of the lower leg (knee to ankle)

# Simulation loop
while robot.step(time_step) != -1:
    # Inverse Kinematics: Compute the joint angles

    # Distance from hip to target
    d_target = math.sqrt(x_target ** 2 + y_target ** 2 + z_target ** 2)

    # Knee pitch (q4) using law of cosines
    q4 = math.acos((L_thigh ** 2 + L_shin ** 2 - d_target ** 2) / (2 * L_thigh * L_shin))

    # Hip pitch (q3) and ankle pitch (q5) from target height and distance
    q3 = -math.atan2(z_target, x_target) - math.atan2(L_shin * math.sin(q4), L_thigh + L_shin * math.cos(q4))
    q5 = -q3 - q4  # Ensure the foot stays horizontal (assuming simplified orientation)

    # Hip roll (q2) from lateral target position
    q2 = math.atan2(y_target, z_target)

    # Hip yaw-pitch (q1) can be set to zero for simplicity (no yaw rotation)
    q1 = 0.0

    # Ankle roll (q6) can also be set to zero for now
    q6 = 0.0

    # Set the computed joint angles
    hip_yaw_pitch.setPosition(q1)
    hip_roll.setPosition(q2)
    hip_pitch.setPosition(q3)
    knee_pitch.setPosition(q4)
    ankle_pitch.setPosition(q5)
    ankle_roll.setPosition(q6)

    # Wait for the next time step
    robot.step(time_step)
