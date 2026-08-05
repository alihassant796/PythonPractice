name= input("Enter your name= ")
print ("welcome", name)

students=["max","leo","harry","john","alax"] 
students.append("ali")
students.remove("max")
print(students)

objects={"pen","marker","pen","marker"}
print(objects)

employe= {
    "name":"alax",
    "age":20,
    "salary":20000
}
print(employe)

marks= int(input("enter your marks="))
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 50:
    print("C")
else: 
     print("fail")

students = [
    {"name": "Ali", "marks": 90},
    {"name": "Ahmed", "marks": 70},
    {"name": "Sara", "marks": 95},
    {"name": "Usman", "marks": 60}
]
for student in students:
    print(student["name"]) 
for student in students:
    if student["marks"] >= 80:
        print (student["name"], student["marks"])
total=0
avg=0
for student in students:
    total=student["marks"]+total
avg=total/4
print (avg) 
highest=students[0] 
for student in students:
    if student["marks"] > highest["marks"]:
        highest=student
print(highest)        