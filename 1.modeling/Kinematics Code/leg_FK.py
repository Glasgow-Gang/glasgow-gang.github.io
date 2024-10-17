import numpy as np

# Define the DH transformation matrix function
def dh_transform(theta, d, a, alpha):
    return np.array([
        [np.cos(theta), -np.sin(theta)*np.cos(alpha), np.sin(theta)*np.sin(alpha), a*np.cos(theta)],
        [np.sin(theta), np.cos(theta)*np.cos(alpha), -np.cos(theta)*np.sin(alpha), a*np.sin(theta)],
        [0, np.sin(alpha), np.cos(alpha), d],
        [0, 0, 0, 1]
    ])

# Define the joint angles (in radians)
q1 = np.radians(0)   # Hip yaw
q2 = np.radians(0)   # Hip roll
q3 = np.radians(-30) # Hip pitch
q4 = np.radians(45)  # Knee pitch
q5 = np.radians(-30) # Ankle pitch
q6 = np.radians(0)   # Ankle roll

# Link lengths (in meters)
L1 = 0.1  # Thigh length
L2 = 0.1  # Shin length
L3 = 0.05 # Foot length

# Compute individual transformation matrices
T1 = dh_transform(q1, 0, 0, np.pi/2)
T2 = dh_transform(q2, 0, 0, np.pi/2)
T3 = dh_transform(q3, L1, 0, 0)
T4 = dh_transform(q4, L2, 0, 0)
T5 = dh_transform(q5, 0, 0, 0)
T6 = dh_transform(q6, L3, 0, np.pi/2)

# Total transformation matrix
T_foot = T1 @ T2 @ T3 @ T4 @ T5 @ T6

# Extract the foot position from the final transformation matrix
foot_position = T_foot[:3, 3]
foot_orientation = T_foot[:3, :3]  # The rotation part of the matrix

# Output the results
print("Foot position (x, y, z):", foot_position)
print("Foot orientation (rotation matrix):\n", foot_orientation)
