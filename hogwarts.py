# students =["Hermione", "Harry", "Ron", "Draco"]
# houses = [
#     "Gryffindor"
#     "Gryffindor"
#     "Gryffindor"
#     "Slytherine"
#     ]

# print(students[0])
# print(students[1])
# print(students[2])

# for student in students:
#     print(student)

# using i for index
# for i in range(len(students)):
#     print(i+1, students[i])

# dictionaries 

# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco":"Slytherine" 
# }

# print(students["Hermione"])

# for student in students:
#     print(student,students[student], sep=", House ")

# More Data
students = [
    {
        'name': "Hermione",
        'house': "Gryffindor",
        'patronus': "Otter"
    },
    {
        'name': "Harry",
        'house': "Gryffindor",
        'patronus': "Stag"
    },
    {
        'name': "Ron",
        'house': "Gryffindor",
        'patronus': "Jack Russle Terrier"
    },
    {
        'name': "Draco",
        'house': "Slytherine",
        'patronus': None
    },
]

# for student in students:
#     print(student["name"], student["house"], student["patronus"], sep=", ")

# with a nested loop
# for student in students:
#     for key in student:
#         print(key, student[key])
#     print("\n")