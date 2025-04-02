# student = {
#     "name":"enock",
#     "age": 30,
#     "is_student": True

# }
#attributes -properties of an object
# human = {
#     "tribe":"kikuyu",
#     "is_alive": True,
    
# }
#class - is a blueprint for creating objects
class student:
    def __init__(self, name, age, id_no,courses):
        self.name = name
        self.age = age
        self.courses = courses
        self.id_no = id_no
enock = student("enock",20,id_no="2233",courses=["python","java"])
rop = student("rop", 25, id_no="2234", courses=["python","java"])
print(f"student name is {enock.name},and age is {enock.age}")
print(f"student name is {rop.name},and age is {rop.age},courses are {rop.courses}")