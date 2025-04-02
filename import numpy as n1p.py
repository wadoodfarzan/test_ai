import numpy as np

# Create a 3D NumPy array of shape (4, 5, 20)
actual_values = np.arange(4 * 5 * 20).reshape(4, 5, 20)

print("Original Shape:", actual_values.shape)
print("\nOriginal Array:")
print(actual_values)

# Apply the slice
result = actual_values[:, :3, 17:]

print("\nSliced Shape:", result.shape)
print("\nSliced Array:")
print(result)
