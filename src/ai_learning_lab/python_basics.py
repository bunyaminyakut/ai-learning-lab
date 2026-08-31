# Basit Python temelleri örnekleri

# --- List ---
fruits = ["apple", "banana", "cherry", "date"]
print("Fruit count:", len(fruits))
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# --- Slicing ---
print("First two fruits:", fruits[:2])
print("Last two fruits:", fruits[-2:])
print("Middle fruits:", fruits[1:3])

# --- Dict ---
person = {
    "name": "Ada",
    "age": 30,
    "city": "Istanbul",
}

# --- Dict üzerinde .items() ile döngü ---
for key, value in person.items():
    print(f"{key}: {value}")
