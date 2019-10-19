from course import Course

class CourseNote:
    def __init__(self, title, noteLink, rating, student, course):
        self.__title = title
        self.__noteLink = noteLink
        self.__rating = rating
        self.__student = student
        self.__course = course
    
    @property
    def getTitle(self):
        return self.__title

    @property
    def getNoteLink(self):
        return self.__noteLink

    @property
    def getRating(self):
        return self.__rating

    @property
    def getStudent(self):
        return self.__student

    @property
    def getCourse(self):
        return self.__course

    def Upvote(self):
        self.rating = self.__rating + 1
    
    def Downvote(self):
        if (self.__rating -1 < 0):
            print("can't have negative votes")
        else:
            self.rating = self.__rating - 1
    
    def __str__(self):
        output = "title: " + self.getTitle + "\n"
        output += "noteLink: " + self.getNoteLink + "\n"
        output += "rating: " + str(self.getRating) + "\n"
        output += "student: " + self.getStudent.getName + "\n"
        output += "course: " + self.getCourse.getCourseCode + "\n"

        return output