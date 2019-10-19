class Course:
    def __init__(self, courseCode):
        self.__courseCode = courseCode
        self.__students = []
        self.__courseNotes = []

    @property
    def getCourseCode(self):
        return self.__courseCode

    @property
    def getStudents(self):
        return self.__students

    @property
    def getCourseNotes(self):
        return self.__courseNotes
    
    def addStudent(self, student):
        self.__students.append(student)
    
    def addCourseNote(self, courseNote):
        self.__courseNotes.append(courseNote)

    def __str__(self):
        output = "CourseCode: " + self.getCourseCode + "\n" +  "Has students: \n" 

        for student in self.getStudents:
            output += student.getZID + "\n"

        output += "CourseNotes:\n"
        for note in self.__courseNotes:
            output += note.getTitle + "\n"
        return output