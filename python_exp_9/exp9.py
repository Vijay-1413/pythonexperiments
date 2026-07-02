import json

data = {
    "id": 1,
    "studentname": "Vijay",
    "email": "vijay@gmail.com",
    "phone": "9876543210"
}

with open("student.json", "w") as file:
    json.dump(data, file, indent=4)

print("Data written to student.json")