import numpy as np

# Leg parameters
L1 = 0.35  # Length of the thigh (upper leg)
L2 = 0.35  # Length of the shin (lower leg)

# Target foot position in Cartesian coordinates
x_f = 0.1  # meters
y_f = 0.0  # meters (assuming no lateral movement)
z_f = -0.5  # meters (below the hip)

# Step 1: Distance to the target foot position
d = np.sqrt(x_f**2 + z_f**2)

# Step 2: Compute the knee angle (q4) using the law of cosines
q4 = np.arccos((L1**2 + L2**2 - d**2) / (2 * L1 * L2))

# Step 3: Compute the hip pitch angle (q3)
alpha = np.arctan2(z_f, x_f)
beta = np.arccos((L1**2 + d**2 - L2**2) / (2 * L1 * d))
q3 = alpha - beta

# Step 4: Compute the ankle pitch angle (q5)
q5 = - (q3 + q4)  # Assuming the foot should be flat on the ground

# Hip yaw (q1) and hip roll (q2) are typically 0 for straight walking
q1 = 0.0  # No yaw rotation
q2 = 0.0  # No lateral tilt

# Ankle roll (q6) is also 0 for a flat foot on the ground
q6 = 0.0

# Output the joint angles
print("Leg Joint Angles (in radians):")
print(f"q1 (Hip Yaw): {q1}")
print(f"q2 (Hip Roll): {q2}")
print(f"q3 (Hip Pitch): {q3}")
print(f"q4 (Knee Pitch): {q4}")
print(f"q5 (Ankle Pitch): {q5}")
print(f"q6 (Ankle Roll): {q6}")
