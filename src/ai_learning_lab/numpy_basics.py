import numpy as np
dataset = np.array([
    [25, 30000, 0],
    [30, 45000, 1],
    [40, 70000, 1],
])

X = dataset[:, :2]
y = dataset[:, 2]

print("X:")
print(X)
print("X shape:", X.shape)

print("y:")
print(y)
print("y shape:", y.shape)

numbers = np.array([1, 2, 3, 4])

print(numbers)
print(type(numbers))
print(numbers.shape)

doubled = numbers * 2

print(doubled)

data = np.array([
    [25, 30000],
    [30, 45000],
    [40, 70000],
])

print(data)
print("Shape:", data.shape)
print("Dimensions:", data.ndim)
