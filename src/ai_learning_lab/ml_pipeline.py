import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


df = pd.read_csv("data/customers.csv")

X = df[["age", "salary"]]
y = df["bought"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y,
)


pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler()),
    ("model", LogisticRegression()),
])


pipeline.fit(X_train, y_train)

predictions = pipeline.predict(X_test)

print("Real answers:")
print(y_test.to_numpy())

print("Predictions:")
print(predictions)

print("Accuracy:", accuracy_score(y_test, predictions))

print("Test data:")
print(X_test)

results = X_test.copy()
results["actual"] = y_test.to_numpy()
results["prediction"] = predictions

print("\nResults:")
print(results)


matrix = confusion_matrix(y_test, predictions)

print("\nConfusion Matrix:")
print(matrix)

print("Precision:", precision_score(y_test, predictions))
print("Recall:", recall_score(y_test, predictions))
