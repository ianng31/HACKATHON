from back_end.CourseNote import CourseNote

class User:
    def __init__(self, zID, name):
        self.__zID= zID
        self.__name = name
        self.__courseNotes = []

    def getName(self):
        return self.__vname

    def getZID(self):
        return self.__zID

    def getCourseNotes(self):
        return self.__courseNotes

    def addCourseNotes(self, courseNote):
        self.__courseNotes.append(courseNote)




