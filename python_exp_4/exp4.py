text = "I am Vijay from Erode"

words = text.split()

data = {}

for i in range(len(words)):
    data[i] = words[i]

print(data)