file = open("sample.txt", "r")

print("Initial position:", file.tell())

# Move pointer to 5th byte
file.seek(5)
print("After seek(5):", file.tell())

# Read from new position
data = file.read()
print("Data after seek:", data)

file.close()