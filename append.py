# Writing data to file
file = open("sample.txt", "w")
file.write("Hello, this is first line.\n")
file.close()

# Appending data to same file
file = open("sample.txt", "a")
file.write("This line is appended.\n")
file.close()

print("Data written and appended successfully.")