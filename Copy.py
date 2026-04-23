# Open source file
source = open("sample.txt", "r")

# Open destination file
destination = open("copy.txt", "w")

# Copy content
data = source.read()
destination.write(data)

# Close files
source.close()
destination.close()

print("File copied successfully.")