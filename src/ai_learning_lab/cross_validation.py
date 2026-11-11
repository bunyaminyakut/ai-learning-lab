from sklearn.datasets import load_breast_cancer
from sklearn.metrics import (
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import cross_val_predict

data = load_breast_cancer()

X = data.data
y = data.target

print("X shape:", X.shape)
print("y shape:", y.shape)

print("Target names:", data.target_names)
print("Feature count:", len(data.feature_names))

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=5000)),
])

scores = cross_val_score(
    pipeline,
    X,
    y,
    cv=5,
)

print("Scores:", scores)
print("Average score:", scores.mean())

predictions = cross_val_predict(
    pipeline,
    X,
    y,
    cv=5,
)

print("\nConfusion Matrix:")
print(confusion_matrix(y, predictions))

print("Precision:", precision_score(y, predictions))
print("Recall:", recall_score(y, predictions))
print("F1:", f1_score(y, predictions))
