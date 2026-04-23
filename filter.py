import pandas as pd

data = {
    "Name": ["A", "B", "C", "A"],
    "Marks": [80, 90, 70, 85]
}

df = pd.DataFrame(data)

# Filter
filtered = df[df["Marks"] > 75]
print("Filtered Data:")
print(filtered)

# Group
grouped = df.groupby("Name").mean()
print("Grouped Data:")
print(grouped)