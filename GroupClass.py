from canvasapi import Canvas
from StudentClass import Student

class Group:
    # a group HAS a name
    # a group HAS and ID
    # a group HAS students
    # a group HAS interactions between students
    
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
    
    # add Interactions to each student in the Group
    def addInteractions(self, sub_dict):
        for student in self.students:
            # get the list of Interactions for that particular Student
            try: 
                stud_inters = sub_dict[student.ID]
                # print(student.getID()) # why is this None?
                # print(student.ID)

                # set that Student attribute
                student.setInteractions(stud_inters)
                print("Student", student.ID, "DOES have interactions on file")
            except:
                print("Student", student.ID, "doesn't have interactions on file")

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