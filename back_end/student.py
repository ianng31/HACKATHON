from coursenote import CourseNote

class Student:
    def __init__(self, zID, name):
        self.__zID= zID
        self.__name = name
        self.__courseNotes = []

    @property
    def getName(self):
        return self.__name

    @property
    def getZID(self):
        return self.__zID

    def getCourseNotes(self):
        return self.__courseNotes

    def addCourseNote(self, courseNote):
        self.__courseNotes.append(courseNote)
    
    def __str__(self):
        output = "zID: " + self.getZID + "\n" + "Name: " + self.getName + "\n"
        output += "CourseNotes:\n"
        for note in self.__courseNotes:
            output += note.getTitle + "\n"
        return output




