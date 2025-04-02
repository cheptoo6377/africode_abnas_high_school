#class - is a blueprint for creating objects
#methods is function defined inside a class
class student:
    def __init__(self, name, age,scores=[], id_no= None,courses=[]):
        self.name = name
        self.age = age
        self.courses = courses
        self.id_no = id_no
        self.scores = scores
    def passed(self):
        if self.scores >= 50:
            return True
        else:
            return False

    def is_active(self):
        if self.courses == []:
            return "not enrolled" 
        else:
            return "enrolled"  
enock = student("enock",20,id_no="2233",courses=[],scores=60)
print(f"student name is {enock.name},and age is {enock.age},scores are {enock.scores},passed is {enock.passed()},is active is {enock.is_active()}")   
