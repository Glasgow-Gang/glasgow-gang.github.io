from controller import Robot, Motor
import math

# Initialize the robot
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Define motor names for NAO's leg joints
joint_names = [
    "LHipYawPitch", "LHipRoll", "LHipPitch", "LKneePitch", "LAnklePitch", "LAnkleRoll",
    "RHipYawPitch", "RHipRoll", "RHipPitch", "RKneePitch", "RAnklePitch", "RAnkleRoll"
]

# Get motor devices
motors = {}
for joint_name in joint_names:
    motor = robot.getDevice(joint_name)
    motor.setPosition(0)  # Set initial position
    motors[joint_name] = motor

# Define a basic walking gait cycle with higher hips (reduced hip pitch)
gait_cycle = [
    # Left leg [HipYawPitch, HipRoll, HipPitch, KneePitch, AnklePitch, AnkleRoll]
    # Right leg [HipYawPitch, HipRoll, HipPitch, KneePitch, AnklePitch, AnkleRoll]
    [[0, 0.05, -0.15, 0.4, -0.2, 0.05], [0, -0.05, -0.15, 0.4, -0.2, -0.05]],
    [[0, -0.05, -0.05, 0.3, -0.15, -0.05], [0, 0.05, -0.25, 0.5, -0.25, 0.05]],
    [[0, 0.05, -0.25, 0.5, -0.25, 0.05], [0, -0.05, -0.05, 0.3, -0.15, -0.05]],
    [[0, -0.05, -0.15, 0.4, -0.2, -0.05], [0, 0.05, -0.15, 0.4, -0.2, 0.05]],
]

# Main control loop
step = 0
while robot.step(timestep) != -1:
    # Set joint positions based on the current step in the gait cycle
    left_leg_angles, right_leg_angles = gait_cycle[step % len(gait_cycle)]
    
    # Set left leg joint positions
    motors["LHipYawPitch"].setPosition(left_leg_angles[0])
    motors["LHipRoll"].setPosition(left_leg_angles[1])
    motors["LHipPitch"].setPosition(left_leg_angles[2])
    motors["LKneePitch"].setPosition(left_leg_angles[3])
    motors["LAnklePitch"].setPosition(left_leg_angles[4])
    motors["LAnkleRoll"].setPosition(left_leg_angles[5])
    
    # Set right leg joint positions
    motors["RHipYawPitch"].setPosition(right_leg_angles[0])
    motors["RHipRoll"].setPosition(right_leg_angles[1])
    motors["RHipPitch"].setPosition(right_leg_angles[2])
    motors["RKneePitch"].setPosition(right_leg_angles[3])
    motors["RAnklePitch"].setPosition(right_leg_angles[4])
    motors["RAnkleRoll"].setPosition(right_leg_angles[5])
    
    # Increment the step to cycle through the gait pattern
    step += 1
