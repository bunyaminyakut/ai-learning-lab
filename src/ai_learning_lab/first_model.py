import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


X = np.array([
    [20, 2],
    [22, 2.5],
    [25, 3],
    [27, 3.5],
    [30, 4],
    [32, 4.5],
    [35, 5],
    [37, 5.5],
    [40, 6],
    [42, 6.5],
    [45, 7],
    [48, 8],
])

y = np.array([
    0, 0, 0, 0, 0, 0,
    1, 1, 1, 1, 1, 1,
])


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
)

model = LogisticRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("X test:")
print(X_test)

print("Real answers:")
print(y_test)

print("Predictions:")
print(predictions)

print("Accuracy:", accuracy_score(y_test, predictions))

