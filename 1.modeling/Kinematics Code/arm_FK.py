import numpy as np


# Helper function to create a transformation matrix given DH parameters
def dh_transform(a, alpha, d, theta):
    return np.array([
        [np.cos(theta), -np.sin(theta) * np.cos(alpha), np.sin(theta) * np.sin(alpha), a * np.cos(theta)],
        [np.sin(theta), np.cos(theta) * np.cos(alpha), -np.cos(theta) * np.sin(alpha), a * np.sin(theta)],
        [0, np.sin(alpha), np.cos(alpha), d],
        [0, 0, 0, 1]
    ])


# Forward kinematics function for NAO6 arm
def forward_kinematics_arm(q1, q2, q3, q4, q5):
    # Define lengths of arm segments (in meters)
    d1 = 0.1  # Distance from shoulder to shoulder pitch axis
    l1 = 0.1  # Upper arm length
    l2 = 0.12  # Forearm length
    l3 = 0.05  # Hand/wrist length

    # Define DH parameters for each joint
    T1 = dh_transform(0, np.pi / 2, d1, q1)
    T2 = dh_transform(0, np.pi / 2, 0, q2)
    T3 = dh_transform(l1, 0, 0, q3)
    T4 = dh_transform(l2, 0, 0, q4)
    T5 = dh_transform(l3, 0, 0, q5)

    # Multiply the transformation matrices to get the final position
    T_total = T1 @ T2 @ T3 @ T4 @ T5

    # Extract the end-effector position (hand) from the final transformation matrix
    hand_position = T_total[:3, 3]

    return hand_position


# Example: Joint angles in radians
q1, q2, q3, q4, q5 = np.radians([30, 45, 0, 60, 0])

# Compute forward kinematics
hand_position = forward_kinematics_arm(q1, q2, q3, q4, q5)
print(f"Hand position (x, y, z): {hand_position}")
