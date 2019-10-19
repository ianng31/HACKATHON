from back_end.user import User
from back_end.course import Course
from back_end.CourseNote import CourseNote

class CollegeDocs_System():

    #add persistence...
    def __init__(self):
        self.users = []
        self.courses = []

    def addCourse(self, courseCode):
        temp = Course(courseCode)
        courses.append.temp
    
    def addUser(self, zID, name):
        temp = User( zID, name)
        users.append.temp
    
    def enrol(user, course):
        course.addUser(user)

    def addCourseNote(self, title, noteLink, rating, user, course):
        temp = CourseNote(self, title, noteLink, rating, user, course)
        #add to user
        user.addCourseNote(temp)
        #add to course
        course.addCourseNote(temp)

    def getUser(self, zID):
        for user in users
            if (zID = user.getZID)
                return User
        else 
            return "User Not Found"
    
    def getCourse(self, courseCode):
        for course in courses
            if (courseCode = course.getCourseCode)
                return course
        else 
            return "Course Not Found"




