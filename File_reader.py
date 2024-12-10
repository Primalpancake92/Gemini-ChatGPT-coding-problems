file = input("What is the name and extension of the file? ")

with open(file) as f:
    for line in f:
        print(line.rstrip())