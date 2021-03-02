from canvasapi import Canvas

class Student:
    # a student HAS a name
    # a student HAS some identification
    # maybe a student has interactions?
    
    # this is the initializer for classes
    # all class methods have the first argument as "self"
    # it's sort of like the "this" word in C++, except not a pointer
    def __init__(self, canvas_user_object):
        # Student constructor which takes a canvas user object
        # and extracts the information into whatever fields it want
        
        # I'm not sure which fields will be useful or not, but we can
        # extract more / less information later if we choose.
        self.name = canvas_user_object.name
        self.ID = canvas_user_object.id
        self.SIS = canvas_user_object.sis_user_id
    
    # set the group that the student is in
    def setStudentGroup(self, group_id):
        self.group = group_id
    
    # returns the student's name
    def getName(self):
        return self.name
    
    # returns the student's id
    def getID(self):
        return self.ID
    
    # returns the student's sis user id
    def getSIS(self):
        return self.SIS