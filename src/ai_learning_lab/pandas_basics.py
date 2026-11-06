import pandas as pd

df = pd.read_csv("data/customers.csv")

print(df)

X = df[["age", "salary"]]
y = df["bought"]

print("\nX:")
print(X)

print("\ny:")
print(y)

print("\nFirst rows:")
print(df.head())

print("\nInfo:")
df.info()

print("\nMissing values:")
print(df.isnull().sum())

print("\nDrop missing rows:")
print(df.dropna())

print("\nFill missing salary with mean:")
filled_df = df.copy()
filled_df["salary"] = filled_df["salary"].fillna(filled_df["salary"].mean())

print(filled_df)
