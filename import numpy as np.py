import numpy as np

# a = np.zeros((3, 3))  # Shape (3,3)
# b = np.array([1, 2, 3])  # Shape (3,)
# print(a)
# print(b)
# a[:, 1] = b  # ✅ This works (assigning 3 elements to a column)
# print(a)
# a[0, :] = b  # ✅ This works (assigning 3 elements to a row)
# print(a)
# a[:, :] = b  # ❌ ERROR: Shapes (3,3) and (3,) are incompatible
# print(a)

# # Example of the error:
# a = [np.zeros((224, 224, 3)), np.zeros((224, 224, 3)), np.zeros((224, 224))]
# print(a)
# c = np.array(a)
# print(c)

print(np.zeros((5, 2, 3)))
