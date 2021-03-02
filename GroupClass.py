from canvasapi import Canvas
from StudentClass import Student

class Group:
    # a group HAS students
    # a group HAS interactions between students
    # a group HAS a name
    # a group HAS identification
    
    # initialize Group by passing in canvas group object
    def __init__(self, canvas_group_object):
        self.name = canvas_group_object.name
        self.ID = canvas_group_object.id
        
        self.students = self.getStudentsInGroup(canvas_group_object)
        self.interactions = None # for now

    # get a list of Students in the group and save to self.students
    def getStudentsInGroup(self, canvas_group_object):
        users = canvas_group_object.get_users()
        students = []
        for user in users:
            student = Student(user)
            student.setStudentGroup(self.ID)
            students.append(student)
            # print("Got student '", student.getName(), "' from group '", self.getName(), "'", sep='')
        return students
    
    # check that name, ID, and SIS match; student is in group
    # used to make sure the interactions are with people in the specific group
    # student should be a Student object
    def checkStudentInGroup(self, canvas_group_object, student):
        if student in canvas_group_object.getStudents:
            return True
        else:
            return False

    # get the group's name
    def getName(self):
        return self.name
        
    # get the group's ID
    def getID(self):
        return self.ID
    
    # get the group's students
    def getStudents(self):
        return self.students
    
    def getInteractions(self):
        print("This isn't ready yet")
        return None