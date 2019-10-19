from back_end.user import User

class Course:
    def __init__(self, courseCode):
        self.__courseCode = courseCode
        self.__users = []
        self.__courseNotes = []


    def getCourseCode(self):
        return self.__courseCode

    def getZID(self):
        return self.__users
    
    def addUsers(self, user):
        self.__users.append(user)
    
    def addNotes(self, courseNote)
        self.__courseNotes.append(courseNote)