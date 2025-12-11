#A dictionary is an unordered, mutable collection of key-value pairs

#defined with {key: value}
#keys must be unique
#values can be anything

student = {
    "name": "Olefile",
    "age": 24,
    "country": "South Africa"
}

#Accessing Dictionary Values
print(student["name"])
print(student.get("age"))

#adding a new key:
student["course"] = "Python Basics"
print(student["course"])

#remove last inserted item:
student.popitem()
print(student)

#delete key:
del student["country"]
print(student)


#Dictionary Methods
#keys(), values(), items()

print(student.keys())
print(student.values())
print(student.items())

