from student import Student
from course import Course
from coursenote import CourseNote

class CollegeDocs_System():

    #add persistence...
    def __init__(self):
        self.students = []
        self.courses = []

    def addCourse(self, courseCode):
        temp = Course(courseCode)
        self.courses.append(temp)
    
    def addStudent(self, zID, name):
        temp = Student( zID, name)
        self.students.append(temp)
    
    def enrol(self, student, course):
        course.addStudent(student)

    def addCourseNote(self, title, noteLink, rating, student, course):
        temp = CourseNote(title, noteLink, rating, student, course)
        #add to student
        student.addCourseNote(temp)
        #add to course
        course.addCourseNote(temp)

    def getStudent(self, zID):
        for student in self.students:
            if zID == student.getZID:
                return student
        else: 
            return "Student Not Found"
    
    def getCourse(self, courseCode):
        for course in self.courses:
            if courseCode == course.getCourseCode:
                return course
        else: 
            return "Course Not Found"
    
    def getCourseNote(self, noteLink):
        allnotes = self.getAllNotes()
        for note in allnotes:
            if noteLink == note.getNoteLink:
                return note
        else: 
            return "Note Not Found"
    
    def getAllNotes(self):
        allnotes = []
        for course in self.courses:
            allnotes += course.getCourseNotes
        return allnotes




