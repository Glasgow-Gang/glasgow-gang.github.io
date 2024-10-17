from controller import Robot
import numpy as np
import math

# Initialize the robot
robot = Robot()

# Time step for the simulation (ms)
time_step = int(robot.getBasicTimeStep())

# Get arm joints
shoulder_pitch = robot.getDevice('LShoulderPitch')
shoulder_roll = robot.getDevice('LShoulderRoll')
elbow_yaw = robot.getDevice('LElbowYaw')
elbow_roll = robot.getDevice('LElbowRoll')
wrist_yaw = robot.getDevice('LWristYaw')

# Arm segment lengths (meters)
d1 = 0.1  # Shoulder offset
l1 = 0.1  # Upper arm length
l2 = 0.12  # Forearm length
l3 = 0.05  # Wrist/hand length


# Function for DH transformation matrix
def dh_transform(a, alpha, d, theta):
    return np.array([
        [np.cos(theta), -np.sin(theta) * np.cos(alpha), np.sin(theta) * np.sin(alpha), a * np.cos(theta)],
        [np.sin(theta), np.cos(theta) * np.cos(alpha), -np.cos(theta) * np.sin(alpha), a * np.sin(theta)],
        [0, np.sin(alpha), np.cos(alpha), d],
        [0, 0, 0, 1]
    ])


# Forward kinematics function for NAO6 arm
def forward_kinematics_arm(q1, q2, q3, q4, q5):
    T1 = dh_transform(0, np.pi / 2, d1, q1)
    T2 = dh_transform(0, np.pi / 2, 0, q2)
    T3 = dh_transform(l1, 0, 0, q3)
    T4 = dh_transform(l2, 0, 0, q4)
    T5 = dh_transform(l3, 0, 0, q5)

    # Multiply matrices to get the final transformation
    T_total = T1 @ T2 @ T3 @ T4 @ T5
    hand_position = T_total[:3, 3]  # Extract the hand (end-effector) position

    return hand_position


# Time-based dynamic motion
t = 0.0  # Initialize time variable for dynamic motion
T = 5.0  # Time period for one cycle of motion (in seconds)

# Simulation loop
while robot.step(time_step) != -1:
    t += time_step / 1000.0  # Update time (in seconds)

    # Generate dynamic joint angles (sinusoidal movement)
    q1 = np.radians(30) * np.sin((2 * np.pi / T) * t)  # Shoulder pitch
    q2 = np.radians(45) * np.sin((2 * np.pi / T) * t)  # Shoulder roll
    q3 = np.radians(20) * np.sin((2 * np.pi / T) * t)  # Elbow yaw
    q4 = np.radians(60) * np.sin((2 * np.pi / T) * t)  # Elbow roll
    q5 = np.radians(30) * np.sin((2 * np.pi / T) * t)  # Wrist yaw

    # Compute forward kinematics to get hand position
    hand_position = forward_kinematics_arm(q1, q2, q3, q4, q5)
    print(f"Hand position at time {t:.2f}s: {hand_position}")

    # Apply joint angles to the robot in Webots
    shoulder_pitch.setPosition(q1)
    shoulder_roll.setPosition(q2)
    elbow_yaw.setPosition(q3)
    elbow_roll.setPosition(q4)
    wrist_yaw.setPosition(q5)

    # Step simulation
    robot.step(time_step)
